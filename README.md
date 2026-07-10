# AI Workshop

This repository is the home for a weekly, hands-on AI workshop, from Torch tensors to Large Language Models.

You can complete the workshop in GitHub Codespaces or locally using a VS Code dev container.

## Option 1: GitHub Codespaces

1. Sign in to GitHub and open this repository.
2. Select **Code**, then **Codespaces**.
3. Select **Create codespace on main** and wait for setup to finish.

See [Creating a codespace for a repository](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository) for more detail.

## Option 2: Dev Containers and VS Code

Choose this option if you want to participate on your local machine.

1. Install [Visual Studio Code](https://code.visualstudio.com/download).
2. Install [Docker Desktop](https://docs.docker.com/desktop/) and start it.
3. In VS Code, install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
4. Clone this repository and open its folder in VS Code.
5. Open the Command Palette (`F1`), run **Dev Containers: Reopen in Container**, and wait for setup to finish.

## Workshop Path

| Session | Topic | Outcome |
| --- | --- | --- |
| 01 | [Setup](01-setup/README.md) | Start the development environment and run a Python script and notebook in VS Code. |
| 02 | [Tensors and PyTorch](02-tensors-and-pytorch/README.md) | Create tensors, inspect shapes, and run basic PyTorch operations. |
| 03 | [MLP MNIST Training Loop](03-mlp-mnist-training-loop/README.md) | Train a small neural network on MNIST using a PyTorch training loop. |
| 04 | [Training Loop Improvements](04-training-loop-improvements/README.md) | Add validation, metrics, checkpoints, and cleaner training structure. |
| 05 | [Hugging Face Basics](05-hugging-face-basics/README.md) | Use tokenizers, datasets, pretrained models, and the model hub. |
| 06 | [Generative Models](06-generative-models/README.md) | Run small pretrained generative models. |
| 07 | [Fine-Tuning Generative Models](07-fine-tuning-generative-models/README.md) | Adapt a small generative model with a focused training loop. |
| 08 | [Advanced vLLM Instruction Tuning](08-advanced-vllm-instruction-tuning/README.md) | Explore instruction-tuning and vLLM workflows for suitable GPU environments. |
