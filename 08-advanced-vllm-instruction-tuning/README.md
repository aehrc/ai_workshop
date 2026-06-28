# 08 - Advanced vLLM Instruction Tuning

## Goal

This is an advanced session. It is not part of the CPU-only core path.

By the end of this session, participants should understand what instruction tuning is, why it usually needs stronger hardware, and where vLLM fits into serving and working with LLMs.

## Hardware Note

vLLM is mainly intended for Linux/CUDA or cloud GPU environments. Many laptops, including many MacBooks and Windows machines without supported NVIDIA GPUs, should treat this as a demonstration or cloud workflow.

## Preparation

Review the language model intuition resources in [05 - Hugging Face Basics](../05-hugging-face-basics/README.md).

## Live Session Outline

1. Review the difference between pretraining, fine-tuning, and instruction tuning.
2. Inspect an instruction-style dataset.
3. Discuss local versus cloud GPU constraints.
4. Run or review a small instruction-tuning workflow.
5. Use vLLM for serving or fast inference where hardware permits.

## Exercises

Exercises will depend on available hardware. CPU-only participants can inspect datasets and run small inference examples; GPU participants can run the advanced workflow.
