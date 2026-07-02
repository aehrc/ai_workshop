from __future__ import annotations

import importlib.util
import os
import platform
import sys


def package_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def print_check(label: str, passed: bool, detail: str = "") -> None:
    status = "PASS" if passed else "WARN"
    suffix = f" - {detail}" if detail else ""
    print(f"[{status}] {label}{suffix}")


def main() -> None:
    print("AI workshop environment check")
    print("=" * 34)
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Executable: {sys.executable}")
    print()

    python_ok = sys.version_info >= (3, 12)
    print_check("Python version is 3.12 or newer", python_ok)

    in_codespaces = os.environ.get("CODESPACES") == "true"
    codespace_name = os.environ.get("CODESPACE_NAME", "")
    detail = codespace_name if codespace_name else "CODESPACES=true"
    print_check("Running in GitHub Codespaces", in_codespaces, detail if in_codespaces else "")
    print()

    packages = [
        "torch",
        "torchvision",
        "torchaudio",
        "jupyter",
        "ipykernel",
        "matplotlib",
        "numpy",
        "pandas",
        "sklearn",
        "tqdm",
        "transformers",
        "datasets",
        "accelerate",
    ]

    for package in packages:
        print_check(f"Package import available: {package}", package_available(package))

    print()

    if not package_available("torch"):
        print("[WARN] PyTorch is not installed, so device detection was skipped.")
        print("Wait for Codespaces setup to finish, or run: python -m pip install -r requirements.txt")
        return

    import torch

    print(f"PyTorch: {torch.__version__}")

    if torch.cuda.is_available():
        device = torch.device("cuda")
        detail = torch.cuda.get_device_name(0)
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        detail = "Apple Metal Performance Shaders"
    else:
        device = torch.device("cpu")
        detail = "CPU fallback"

    print_check("PyTorch device detected", True, f"{device} ({detail})")

    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = x * 2
    print(f"Tensor check: {y.cpu().tolist()}")
    print()
    print("Environment check complete.")


if __name__ == "__main__":
    main()
