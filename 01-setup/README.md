# 01 - Setup

## Goal

By the end of this session, you should be able to:

- install Python
- install VS Code
- install Git
- clone the workshop repository from GitHub
- install the VS Code Python and Jupyter extensions
- open this repository in VS Code
- create and activate a Python virtual environment
- install the workshop packages
- run a Python script
- run a notebook
- identify whether PyTorch sees CPU, Apple MPS, or CUDA

## 1. Install Python

Install Python from:

https://www.python.org/downloads/

Use Python 3.12 for this workshop. It is stable and well supported by the packages we will use.

### Windows

When running the Python installer, tick:

```text
Add python.exe to PATH
```

Then continue with the default installation.

After installation, close and reopen PowerShell.

Check Python is available:

```powershell
python --version
```

If that does not work, try:

```powershell
py --version
```

### macOS

macOS may already include a system Python, but it may be too old for this workshop. Install a current Python from:

https://www.python.org/downloads/macos/

After installation, close and reopen Terminal.

Check Python is available:

```bash
python3 --version
```

Some Macs will not have a `python` command. That is okay. Use `python3` for the setup commands if `python` does not work.

## 2. Install VS Code

Install Visual Studio Code from:

https://code.visualstudio.com/

After installing VS Code, open it once so it can finish its first-run setup.

## 3. Install Git

Git is the tool we will use to download the workshop repository from GitHub.

Check whether Git is already installed:

```bash
git --version
```

If Git is installed, the command prints a version number.

If Git is not installed, install it from:

https://git-scm.com/downloads

### Windows

Use the Git for Windows installer:

https://git-scm.com/download/win

The default installer options are fine for this workshop.

After installation, close and reopen PowerShell, then check:

```powershell
git --version
```

### macOS

Run:

```bash
git --version
```

If macOS asks you to install command line developer tools, accept the prompt and let the installation finish.

You can also install Git from:

https://git-scm.com/download/mac

After installation, close and reopen Terminal, then check:

```bash
git --version
```

## 4. Clone the Workshop Repository

Choose a place on your laptop where you keep code projects. For example, you might create a `workshops` folder.

In Terminal or PowerShell, move to that folder, then run:

```bash
git clone https://github.com/aehrc/ai_workshop.git
```

Move into the repository:

```bash
cd ai_workshop
```

You should now be in the folder that contains `requirements.txt`.

## 5. Install VS Code Extensions

Open VS Code, then install these extensions:

- Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Jupyter: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

You can install extensions from the Extensions panel in VS Code. Search for `Python` and `Jupyter`, then install the Microsoft extensions.

## 6. Open the Repository

Open the cloned `ai_workshop` folder in VS Code.

If VS Code asks whether you trust the authors of the files in this folder, choose to trust the workspace.

Open the integrated terminal in VS Code:

- macOS: `Terminal > New Terminal`
- Windows: `Terminal > New Terminal`

Run the remaining commands from the repository root. The repository root is the folder that contains `requirements.txt`.

## 7. Create a Virtual Environment

From the repository root, run:

```bash
python -m venv .venv
```

If `python` does not work on macOS, run:

```bash
python3 -m venv .venv
```

If `python` does not work on Windows, run:

```powershell
py -m venv .venv
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal prompt should usually include `.venv`.

## 8. Select the VS Code Python Interpreter

In VS Code:

1. Open the Command Palette:
   - macOS: `Cmd+Shift+P`
   - Windows: `Ctrl+Shift+P`
2. Search for `Python: Select Interpreter`.
3. Choose the interpreter inside `.venv`.

It will usually look like one of these:

```text
.venv/bin/python
.venv\Scripts\python.exe
```

## 9. Install Packages

With the virtual environment active, run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you used `python3` or `py` to create the virtual environment, activate `.venv` first, then try the same `python -m pip ...` commands. Inside an active virtual environment, `python` should usually work.

This may take several minutes.

## 10. Check the Environment

Run:

```bash
python 01-setup/check_environment.py
```

Expected result: the script prints your Python version, virtual environment status, key package availability, and the best PyTorch device available on your machine.

CPU is acceptable.

## 11. Run a Python Script

Run:

```bash
python 01-setup/hello_torch.py
```

Expected result: the script creates a tensor, runs a small calculation, and prints the device PyTorch is using.

## 12. Run a Notebook in VS Code

Open:

```text
01-setup/hello_notebook.ipynb
```

Select the `.venv` kernel when VS Code asks. Run each cell from top to bottom.

Expected result: the notebook imports PyTorch and runs a small tensor calculation.

## Troubleshooting

### Python command not found

Try:

```bash
python3 --version
```

On Windows, try:

```powershell
py --version
```

If none of these work, Python is not installed correctly or your terminal was opened before Python was installed. Close and reopen the terminal.

### Git command not found

Try closing and reopening the terminal first.

If Git still does not work, install it from:

https://git-scm.com/downloads

Then check:

```bash
git --version
```

### Clone fails

Check:

- the clone command was copied exactly
- your internet connection is working
- Git is installed and available in the terminal
- the repository URL is `https://github.com/aehrc/ai_workshop.git`

### VS Code cannot find `.venv`

Make sure:

- the virtual environment was created from the repository root
- the `.venv` folder exists
- you selected the interpreter using `Python: Select Interpreter`

### Package installation fails

If package installation fails, check:

- the virtual environment is active
- Python is version 3.12
- VS Code selected the `.venv` interpreter
- your terminal is running from the repository root

### Notebook kernel is missing

If VS Code asks for a notebook kernel, choose the `.venv` environment.

If it does not appear:

```bash
python -m pip install ipykernel
```

Then reload VS Code and try again.

### No GPU is detected

If GPU acceleration is not available, continue with CPU. The core workshop path is designed for CPU.
