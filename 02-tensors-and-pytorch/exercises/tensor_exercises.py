from __future__ import annotations

import torch


def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def todo(name: str) -> None:
    raise NotImplementedError(f"TODO: complete {name}")


def make_feature_vector() -> torch.Tensor:
    """Return a float tensor containing 2.0, 4.0, and 6.0."""
    todo("make_feature_vector")


def make_batch() -> torch.Tensor:
    """Return a 3 x 2 float tensor from the values 1.0 through 6.0."""
    todo("make_batch")


def first_example(batch: torch.Tensor) -> torch.Tensor:
    """Return the first row from a batch."""
    todo("first_example")


def predict_scores(batch: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
    """Return matrix multiplication between a batch and weights."""
    todo("predict_scores")


def example_totals(batch: torch.Tensor) -> torch.Tensor:
    """Return the sum of each example across its features."""
    todo("example_totals")


def move_to_available_device(tensor: torch.Tensor) -> torch.Tensor:
    """Move tensor to CUDA, MPS, or CPU, depending on what is available."""
    todo("move_to_available_device")


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"Check failed: {name}")
    print(f"PASS: {name}")


def main() -> None:
    features = make_feature_vector()
    check("feature vector is a tensor", isinstance(features, torch.Tensor))
    check("feature vector has shape (3,)", tuple(features.shape) == (3,))
    check("feature vector uses float32", features.dtype == torch.float32)
    check("feature vector has expected values", torch.equal(features, torch.tensor([2.0, 4.0, 6.0])))

    batch = make_batch()
    check("batch has shape (3, 2)", tuple(batch.shape) == (3, 2))
    check("batch uses float32", batch.dtype == torch.float32)
    check(
        "batch has expected values",
        torch.equal(batch, torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])),
    )

    first = first_example(batch)
    check("first example has shape (2,)", tuple(first.shape) == (2,))
    check("first example has expected values", torch.equal(first, torch.tensor([1.0, 2.0])))

    weights = torch.tensor([[0.5, 1.0, -1.0], [2.0, 0.0, 1.0]])
    scores = predict_scores(batch, weights)
    expected_scores = torch.tensor([[4.5, 1.0, 1.0], [9.5, 3.0, 1.0], [14.5, 5.0, 1.0]])
    check("scores has shape (3, 3)", tuple(scores.shape) == (3, 3))
    check("scores has expected values", torch.allclose(scores, expected_scores))

    totals = example_totals(batch)
    check("example totals has shape (3,)", tuple(totals.shape) == (3,))
    check("example totals has expected values", torch.equal(totals, torch.tensor([3.0, 7.0, 11.0])))

    moved = move_to_available_device(batch)
    check("moved tensor stays equal on CPU", torch.equal(moved.cpu(), batch))
    check("moved tensor is on expected device", moved.device.type == get_device().type)

    print()
    print("All tensor exercise checks passed.")


if __name__ == "__main__":
    main()
