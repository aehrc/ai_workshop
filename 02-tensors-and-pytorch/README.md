# 02 - Tensors and PyTorch

## Neural Network Intuition

Recommended preparation before this lesson:

- https://www.youtube.com/watch?v=aircAruvnKk
- https://www.youtube.com/watch?v=IHZwWFHWa-w
- https://www.youtube.com/watch?v=Ilg3gGewQ5U
- https://www.youtube.com/watch?v=tIeHLnjs5U8

## Goal

In this session, we will:

- Create PyTorch tensors
- Inspect tensor shapes and data types
- Move tensors to the available device
- Perform basic tensor operations
- Understand why tensor shape errors are common in machine learning code

## Files

- [tensor_walkthrough.py](tensor_walkthrough.py): live-coding script for the instructor
- [exercises/tensor_exercises.py](exercises/tensor_exercises.py): participant exercise file with TODOs and built-in checks
- [solutions/tensor_exercises_solution.py](solutions/tensor_exercises_solution.py): completed exercise file

## Live Session Outline

This is designed to fit either a 45-60 minute session or a 15-25 minute "extra time" version after setup.

### Short Version

1. Run the walkthrough:

   ```bash
   python 02-tensors-and-pytorch/tensor_walkthrough.py
   ```

2. Point out:
   - tensors have shape, dtype, and device
   - matrix multiplication requires matching inner dimensions
   - neural network batches are usually shaped as `batch_size x features`
   - models often fail because a tensor has the right numbers in the wrong shape

3. Start the exercises:

   ```bash
   python 02-tensors-and-pytorch/exercises/tensor_exercises.py
   ```

4. Participants fill in one TODO at a time and rerun the script until all checks pass.

### Full Version

1. Create tensors from Python lists.
2. Inspect `.shape`, `.dtype`, and `.device`.
3. Select CPU, CUDA, or MPS using `get_device()`.
4. Run indexing, reshaping, matrix multiplication, and reductions.
5. Interpret a tiny batch of tabular features.
6. Complete the exercise file individually or in pairs.
7. Review the solution file:

   ```bash
   python 02-tensors-and-pytorch/solutions/tensor_exercises_solution.py
   ```

## Instructor Notes

Use concrete language before introducing neural-network terminology:

- A scalar has no dimensions: one number.
- A vector has one dimension: a list of numbers.
- A matrix has two dimensions: rows and columns.
- A batch adds a leading dimension: several examples at once.

Useful prompts:

- What shape do you expect before running this line?
- Which dimension means examples?
- Which dimension means input features?
- Why does `x @ weights` work, but `weights @ x` fail?
- What changes when the tensor moves from CPU to MPS or CUDA?

## Exercises

Exercises focus on:

1. Creating tensors with the expected dtype.
2. Inspecting shape and dtype.
3. Reshaping flat values into a batch.
4. Running matrix multiplication.
5. Reducing across the right dimension.
6. Moving tensors to the detected device.
