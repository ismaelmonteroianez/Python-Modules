import importlib
from typing import Any


def print_error(modules: dict[str, Any]) -> None:
    for key, value in modules.items():
        if value is None:
            print()
            print(f"[ERROR] {key} is missing")
            print("Install with pip:")
            print(f"pip install {key}")
            print()
            print("or install all dependencies:")
            print("pip install -r requirements.txt")
            break


def create_visualization(modules: dict[str, Any], modules_check: bool) -> None:
    if modules_check:
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
    else:
        print_error(modules)


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    imports = ["pandas", "numpy", "requests",
               "matplotlib", "matplotlib.pyplot"]
    modules: dict[str, Any] = {}
    for i in imports:
        try:
            module = importlib.import_module(i)
            modules[i] = module
        except ModuleNotFoundError:
            modules[i] = None
    required = ["pandas", "numpy", "matplotlib"]
    modules_check = True
    for name in required:
        if modules[name] is None:
            modules_check = False
    print("Checking dependencies:")
    if modules["pandas"] is not None:
        print(f"[OK] pandas ({modules['pandas'].__version__})"
              " - Data manipulation ready")
    if modules["numpy"] is not None:
        print(f"[OK] numpy ({modules['numpy'].__version__})"
              " - Numerical computation ready")
    if modules["requests"] is not None:
        print(f"[OK] requests ({modules['requests'].__version__})"
              " - Network access ready")
    if modules["matplotlib"] is not None:
        print(f"[OK] matplotlib ({modules['matplotlib'].__version__})"
              " - Visualization ready")
    create_visualization(modules, modules_check)


if __name__ == "__main__":
    main()
