 
import os
from google.genai import types
from config import MAX_CHARS

def get_files_content(working_directory, file_path):
  abs_working_dir=os.path.abspath(working_directory)

  if file_path is None or file_path ==".":
    abs_file_path=os.path.abspath(working_directory)
  else:
   abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))
    
  if not abs_file_path.startswith(abs_working_dir):
    return f"Error: '{file_path}' is not a directory"
  if not os.path.isfile(abs_file_path):
    return f"Error: '{file_path}' is not a file"
  file_content=""
  try:
    with open(abs_file_path,"r") as f:
      file_content=f.read(MAX_CHARS)
      if len(file_content)>=MAX_CHARS:
        file_content+=f"[...File '{file_path}' truncated at 10000 chars]"
    return file_content 
  except Exception as e:
    return f"Exception reading file:'{e}"

schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Gets contents of the given file as a string,constrained to working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files form relative to the working directory.(default lists files in the working  directory itself)",
            ),
        },
    ),
)  


  