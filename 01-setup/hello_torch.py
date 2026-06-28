from __future__ import annotations

import torch


def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def main() -> None:
    device = get_device()

    x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device)
    weights = torch.tensor([[0.5], [1.5]], device=device)
    result = x @ weights

    print(f"Using device: {device}")
    print("Input tensor:")
    print(x.cpu())
    print("Result:")
    print(result.cpu())


if __name__ == "__main__":
    main()
