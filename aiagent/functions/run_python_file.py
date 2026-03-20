import os
import subprocess
from google.genai import types

def run_file(working_directory:str,file_path:str,args=[]):
  abs_working_dir=os.path.abspath(working_directory)

  if file_path is None or file_path ==".":
    abs_file_path=os.path.abspath(working_directory)
  else:
   abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))
    
  if not abs_file_path.startswith(abs_working_dir):
    return f"Error: '{file_path}' is not a directory"
  if not os.path.isfile(abs_file_path):
    return f"Error: '{file_path}' is not a file"
  if not file_path.endswith(".py"):
    return f"Error '{file_path}' is not a python file"
  
  try:
          
    final_args= ["python",file_path]
    final_args.extend(args)
    output= subprocess.run(
      final_args,
      cwd=abs_working_dir,
      timeout=30,
      capture_output=True
      )
    fcd=f"""
    STDOUT='{output.stdout}'
    STDERR='{output.stderr},
    """
    if output.stdout=="" and output.stderr=="":
      fcd+="No output produced!\n"
    if output.returncode !=0:
      fcd+= f"Process wxited with returncode: '{output.returncode}'"
    return fcd
  except Exception as e:
    return f'Exception :excetuing Python File :"{e}"'

schema_run_file = types.FunctionDeclaration(
    name="run_file",
    description="Runs a python with python3 interpreter .Accepts additional CLI args as an optional array",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run relative to  working directory.(default lists files in the working  directory itself)",
            ),
           "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the CLI args  for Python file ",
                items=types.Schema(
                  type=types.Type.STRING
                )
            ) },
    ),
)  
                 
                   
                   
                   
                   
                   
                   
                   
                   
                