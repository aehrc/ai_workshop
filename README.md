# AI Workshop

This repository is the home for a weekly, hands-on AI workshop. Sessions are designed for 1 hour each and assume a mix of experience levels.

The core lessons are designed to run on CPU. If a participant has a supported GPU or Apple Silicon acceleration, the setup checks will report it, but GPU access is not required until the advanced vLLM session.

## Workshop Path

| Session | Topic | Outcome |
| --- | --- | --- |
| 01 | [Setup](01-setup/README.md) | Install Python tooling, create a virtual environment, install packages, and run a script and notebook in VS Code. |
| 02 | [Tensors and PyTorch](02-tensors-and-pytorch/README.md) | Create tensors, inspect shapes, and run basic PyTorch operations. |
| 03 | [MLP MNIST Training Loop](03-mlp-mnist-training-loop/README.md) | Train a small neural network on MNIST using a local PyTorch training loop. |
| 04 | [Training Loop Improvements](04-training-loop-improvements/README.md) | Add validation, metrics, checkpoints, and cleaner training structure. |
| 05 | [Hugging Face Basics](05-hugging-face-basics/README.md) | Use tokenizers, datasets, pretrained models, and the model hub. |
| 06 | [Generative Models](06-generative-models/README.md) | Run small pretrained generative models locally. |
| 07 | [Fine-Tuning Generative Models](07-fine-tuning-generative-models/README.md) | Adapt a small generative model with a focused training loop. |
| 08 | [Advanced vLLM Instruction Tuning](08-advanced-vllm-instruction-tuning/README.md) | Explore instruction-tuning and vLLM workflows for suitable GPU or cloud environments. |

## Hardware Expectations

- CPU is enough for the core workshop path.
- Apple Silicon Macs may use MPS acceleration if PyTorch supports the machine.
- Windows/Linux machines may use CUDA if the right NVIDIA drivers and PyTorch build are installed.
- Advanced LLM training and vLLM may require cloud GPU access.

## Repository Shape

Each lesson is a top-level directory. Lessons may include:

- `README.md` for the lesson plan and instructions
- Python scripts for repeatable runs
- notebooks for exploration
- `exercises/` for small incomplete coding tasks
- `solutions/` for completed versions of those tasks

The shared environment for the core sessions is defined in [requirements.txt](requirements.txt). Advanced dependencies are separated in [requirements-advanced.txt](requirements-advanced.txt).
