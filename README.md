# AI Workshop

This repository is the home for a weekly, hands-on AI workshop. Sessions are designed for 1 hour each and assume a mix of experience levels.

The workshop runs in GitHub Codespaces only. Participants use browser-based VS Code with the repository, Python, Jupyter, and workshop packages prepared by the dev container.

The core lessons are designed to run on CPU in Codespaces. GPU access is not required until the advanced vLLM session, which needs a separately arranged GPU-capable environment.

## Start Here

Before the workshop, make sure you can sign in to GitHub.

1. Open this repository on GitHub.
2. Select `Code`.
3. Select the `Codespaces` tab.
4. Select `Create codespace`.
5. Wait for the setup command to finish installing Python packages.
6. Open the Codespaces terminal.
7. Run:

   ```bash
   python 01-setup/check_environment.py
   ```

Use [01 - Setup](01-setup/README.md) for the full first-session walkthrough.

## Workshop Path

| Session | Topic | Outcome |
| --- | --- | --- |
| 01 | [Setup](01-setup/README.md) | Create a Codespace, confirm the environment, and run a Python script and notebook in browser-based VS Code. |
| 02 | [Tensors and PyTorch](02-tensors-and-pytorch/README.md) | Create tensors, inspect shapes, and run basic PyTorch operations. |
| 03 | [MLP MNIST Training Loop](03-mlp-mnist-training-loop/README.md) | Train a small neural network on MNIST using a PyTorch training loop in Codespaces. |
| 04 | [Training Loop Improvements](04-training-loop-improvements/README.md) | Add validation, metrics, checkpoints, and cleaner training structure. |
| 05 | [Hugging Face Basics](05-hugging-face-basics/README.md) | Use tokenizers, datasets, pretrained models, and the model hub. |
| 06 | [Generative Models](06-generative-models/README.md) | Run small pretrained generative models in Codespaces. |
| 07 | [Fine-Tuning Generative Models](07-fine-tuning-generative-models/README.md) | Adapt a small generative model with a focused training loop. |
| 08 | [Advanced vLLM Instruction Tuning](08-advanced-vllm-instruction-tuning/README.md) | Explore instruction-tuning and vLLM workflows for suitable GPU environments. |

## Codespaces Expectations

- A 4-core / 8 GB Codespace is recommended for the full workshop.
- Smaller Codespaces may work for setup and tensor basics, but later sessions can be slower.
- Standard Codespaces are CPU environments.
- Advanced LLM training and vLLM require a separately arranged GPU-capable environment.

## Repository Shape

Each lesson is a top-level directory. Lessons may include:

- `README.md` for the lesson plan and instructions
- Python scripts for repeatable runs
- notebooks for exploration
- `exercises/` for small incomplete coding tasks
- `solutions/` for completed versions of those tasks

The shared environment for the core sessions is defined in [requirements.txt](requirements.txt) and installed automatically when a Codespace is created. Advanced dependencies are separated in [requirements-advanced.txt](requirements-advanced.txt).
