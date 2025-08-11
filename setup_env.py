import sys
import subprocess
import importlib
import random
import numpy as np
import torch
from pathlib import Path

# Function to install a package if it's missing
def install_if_missing(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Read packages from requirements.txt
requirements_path = Path(__file__).parent / "requirements.txt"
with open(requirements_path) as f:
    packages = [
        line.strip() for line in f
        if line.strip() and not line.startswith("#")
    ]

# Install missing packages
for pkg in packages:
    import_name = pkg.split("==")[0].split(">=")[0].split("<=")[0]
    import_name = import_name.replace("-", "_")
    install_if_missing(import_name)

# Set seeds for reproducibility
def set_seeds(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seeds(42)

# Print environment summary
print("\nEnvironment ready. Packages installed if missing, seeds set.")
print("Installed package versions:")
for pkg in packages:
    try:
        mod_name = pkg.split("==")[0].split(">=")[0].split("<=")[0].replace("-", "_")
        mod = importlib.import_module(mod_name)
        version = getattr(mod, "__version__", "unknown")
        print(f"  {pkg} (import as '{mod_name}') → version: {version}")
    except ImportError:
        print(f"  {pkg} not importable after install!")

# GPU and CUDA information
print("\nHardware info:")
if torch.cuda.is_available():
    print(f"GPU available: {torch.cuda.get_device_name(0)}")
    print(f"CUDA version: {torch.version.cuda}")
else:
    print("No GPU detected. Running on CPU.")
