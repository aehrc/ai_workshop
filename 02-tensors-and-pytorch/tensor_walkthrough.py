from __future__ import annotations

import torch


def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def print_section(title: str) -> None:
    print()
    print(title)
    print("=" * len(title))


def describe(name: str, tensor: torch.Tensor) -> None:
    print(f"{name}:")
    print(tensor.cpu())
    print(f"  shape: {tuple(tensor.shape)}")
    print(f"  dtype: {tensor.dtype}")
    print(f"  device: {tensor.device}")


def main() -> None:
    device = get_device()
    print(f"Using device: {device}")

    print_section("1. Creating tensors")
    scalar = torch.tensor(3.14)
    vector = torch.tensor([1.0, 2.0, 3.0])
    matrix = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    describe("scalar", scalar)
    describe("vector", vector)
    describe("matrix", matrix)

    print_section("2. Indexing")
    print(f"First row: {matrix[0].tolist()}")
    print(f"Second row, third column: {matrix[1, 2].item()}")

    print_section("3. Reshaping")
    flat = torch.arange(12)
    batch = flat.reshape(3, 4)
    describe("flat", flat)
    describe("batch", batch)

    print_section("4. Matrix multiplication")
    features = torch.tensor(
        [
            [1.0, 0.0, 2.0],
            [0.0, 1.0, 3.0],
            [1.0, 1.0, 1.0],
        ],
        device=device,
    )
    weights = torch.tensor(
        [
            [0.5, 1.0],
            [1.5, -1.0],
            [2.0, 0.25],
        ],
        device=device,
    )
    scores = features @ weights
    describe("features", features)
    describe("weights", weights)
    describe("scores = features @ weights", scores)

    print_section("5. Reductions")
    row_sums = scores.sum(dim=1)
    column_means = scores.mean(dim=0)
    describe("row_sums", row_sums)
    describe("column_means", column_means)

    print_section("6. Shape mismatch example")
    print("features has shape (3, 3)")
    print("weights has shape (3, 2)")
    print("features @ weights works because the inner dimensions match: 3 and 3")
    print("weights @ features would fail because the inner dimensions are 2 and 3")


if __name__ == "__main__":
    main()
