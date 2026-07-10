# 01 - Setup

In this session, we aim to:

- Create a GitHub Codespace for the workshop repository
- Use browser-based VS Code
- Wait for the dev container to install Python packages
- Open a terminal in Codespaces
- Run a Python script
- Run a notebook
- Confirm PyTorch is available on the Codespaces CPU environment

## 1. Sign In To GitHub

Open:

https://github.com/login

Sign in with your GitHub account.

## 2. Open The Workshop Repository

Open the workshop repository page:

https://github.com/aehrc/ai_workshop

## 3. Create A Codespace

On the repository page:

1. Select `Code`.
2. Select the `Codespaces` tab.
3. Select `Create codespace`.

GitHub will open browser-based VS Code. The first startup can take several minutes because the workshop packages are installed automatically.

Wait until the setup command has finished before running the first script.

## 4. Open The Terminal

In browser-based VS Code, open a terminal:

```text
Terminal > New Terminal
```

The terminal should open at the repository root. The repository root is the folder that contains `requirements.txt`.

## 5. Check The Environment

Run:

```bash
python 01-setup/check_environment.py
```

Expected result: the script prints your Python version, confirms Codespaces, checks that the workshop packages are available, and reports the PyTorch device.

CPU is expected for the core workshop path.

## 6. Run A Python Script

Run:

```bash
python 01-setup/hello_torch.py
```

Expected result: the script creates a tensor, runs a small calculation, and prints the device PyTorch is using.

## 7. Run A Notebook

Open:

```text
01-setup/hello_notebook.ipynb
```

If VS Code asks for a notebook kernel, choose the Python environment from the Codespace container.

Run each cell from top to bottom.

Expected result: the notebook imports PyTorch and runs a small tensor calculation.

## Troubleshooting

### Codespace Setup Is Still Running

If package imports fail immediately after the Codespace opens, wait for the setup command to finish. It installs the packages from `requirements.txt`.

You can rerun the install command manually if needed:

```bash
python -m pip install -r requirements.txt
```

### Terminal Is In The Wrong Folder

Run:

```bash
pwd
```

The path should end with:

```text
ai_workshop
```

If not, run:

```bash
cd /workspaces/ai_workshop
```

### Notebook Kernel Is Missing

If VS Code asks for a notebook kernel, choose the Python environment from the Codespace container.

If it does not appear, run:

```bash
python -m pip install ipykernel
```

Then reload the browser tab and try again.

### No GPU Is Detected

That is expected. The core workshop path is designed for CPU in Codespaces.

The advanced vLLM session requires a separately arranged GPU-capable environment.
