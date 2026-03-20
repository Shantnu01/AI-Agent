# AI Agent (aiagent)

## 🚀 What this project is

`aiagent` is a small local AI assistant framework built around Google Gemini / Gemini API and function calling. It lets you prompt with natural language and automatically execute safe file helper functions (`list files`, `read file`, `write file`, `run Python`).

This repository is made for rapid local code automation, debugging, and developer workflows.

## 🔧 How it works

1. Start with `main.py`, which:
   - loads your Gemini API key from `.env`
   - constructs a system prompt and user prompt
   - registers function declarations (file operations)
   - calls Gemini generate_content with tools
   - receives tool-based function call requests
   - executes the function locally, returns results

2. The function call bridge:
   - `call_function.py` maps names like `get_files_info`, `get_file_content`, `write_file`, `run_python_file`
   - executes helper functions in `functions/`
   - returns structured tool response back to Gemini output.

3. Helper modules in `functions/`:
   - `get_files_info.py` → list directory entries with sizes
   - `get_file_content.py` → read file contents securely
   - `write_file.py` → write/overwrite files safely (working-directory constrained)
   - `run_python_file.py` → run a Python file and return stdout/stderr

4. You run the agent with:
   - `uv run main.py "<your prompt>"`
   - Example: `uv run main.py "create a readme.md file and write calculator in it"`

## 🧠 What you can do

- Ask the agent to inspect your code files
- Ask it to create or edit files with safe function calls
- Run test scripts and capture output
- Build automation for simple dev tasks from natural language prompts

## ⚠️ Important notes

- This project is currently limited by Gemini API quota; you may get `RESOURCE_EXHAUSTED` if you exceed free-tier limits.
- All file actions are restricted to the working directory for safety.
- Run with Python 3.12 and activate `.venv` first if needed.

## ✅ Quick start

```bash
cd aiagent
source .venv/bin/activate
uv run main.py "create a readme.md file and write 'calculator' in it"
```



### Project structure

- `main.py` — main Gemini agent runner
- `call_function.py` — function call dispatcher
- `functions/` — file helper tool functions
- `tests.py` — local test runner for helpers

Keep this README as your working manual for AI agent usage and future contributions.
