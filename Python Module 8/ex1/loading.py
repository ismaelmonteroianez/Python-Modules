import importlib
from typing import Any


def print_error(modules: dict[str, Any]) -> None:
    missing = []
    for key, value in modules.items():
        if value is None:
            missing.append(key)
    if missing:
        print(" MISSING DEPENDENCIES DETECTED")
        print(f" Missing: {', '.join(missing)}")
        print()
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print()
        print("Install with Poetry:")
        print("poetry install")


def create_visualization(modules: dict[str, Any]) -> None:
    print("Analyzing Matrix data...")
    intensity_data = modules["numpy"].random.normal(500, 50, 1000)
    data = {"intensity": intensity_data}
    print("Processing 1000 data points...")
    data_table = modules["pandas"].DataFrame(data)
    print("Generating visualization...")
    modules["matplotlib.pyplot"].hist(data_table["intensity"], 40)
    modules["matplotlib.pyplot"].title("Intensity Signal Distribution")
    modules["matplotlib.pyplot"].xlabel("Signal Intensity")
    modules["matplotlib.pyplot"].ylabel("Frequency")
    modules["matplotlib.pyplot"].savefig("matrix_analysis.png")
    modules["matplotlib.pyplot"].close()
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    imports = ["pandas", "numpy", "matplotlib", "matplotlib.pyplot"]
    modules: dict[str, Any] = {}
    for i in imports:
        try:
            module = importlib.import_module(i)
            modules[i] = module
        except ModuleNotFoundError:
            modules[i] = None
    required = ["pandas", "numpy", "matplotlib", "matplotlib.pyplot"]
    modules_check = True
    for name in required:
        if modules[name] is None:
            modules_check = False
    if modules["pandas"] is not None:
        print(f"[OK] pandas ({modules['pandas'].__version__})"
              " - Data manipulation ready")
    if modules["numpy"] is not None:
        print(f"[OK] numpy ({modules['numpy'].__version__})"
              " - Numerical computation ready")
    if modules["matplotlib"] is not None:
        print(f"[OK] matplotlib ({modules['matplotlib'].__version__})"
              " - Visualization ready")
    print("\nDependency Manager Comparison:")
    print("- pip: traditional package manager using requirements.txt")
    print("- Poetry: modern dependency manager"
          " using pyproject.toml and lock files")
    print("- Poetry also manages virtual environments automatically")
    print()
    print("Checking dependencies:")
    if modules_check:
        create_visualization(modules)
    else:
        print_error(modules)


if __name__ == "__main__":
    main()
