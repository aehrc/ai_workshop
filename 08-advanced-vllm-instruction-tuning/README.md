# 08 - Advanced vLLM Instruction Tuning

## Goal

This is an advanced session. It is not part of the CPU-only core path.

By the end of this session, participants should understand what instruction tuning is, why it usually needs stronger hardware, and where vLLM fits into serving and working with LLMs.

## Hardware Note

Standard Codespaces are CPU environments. vLLM is mainly intended for Linux/CUDA or GPU-capable cloud environments, so this session requires a separately arranged GPU environment or should be treated as a demonstration.

## Preparation

Review the language model intuition resources in [05 - Hugging Face Basics](../05-hugging-face-basics/README.md).

## Live Session Outline

1. Review the difference between pretraining, fine-tuning, and instruction tuning.
2. Inspect an instruction-style dataset.
3. Discuss Codespaces CPU constraints versus GPU environment requirements.
4. Run or review a small instruction-tuning workflow.
5. Use vLLM for serving or fast inference where hardware permits.

## Exercises

Exercises will depend on available hardware. Codespaces participants can inspect datasets and run small inference examples; GPU-environment participants can run the advanced workflow.
