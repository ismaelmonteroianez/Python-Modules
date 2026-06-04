import importlib

def main() -> None:
    print("LOADING STATUS: Loading programs...")
    imports = ["pandas", "numpy", "requests", "matplotlib", "matplotlib.pyplot"]
    modules = {}
    for i in imports:
        try:
            module = importlib.import_module(i)
            modules[i] = module
        except ModuleNotFoundError:
            modules[i] = None
    modules_check = True
    print("Checking dependencies:")
    if modules["pandas"] is not None:
        print(f"[OK] pandas ({modules['pandas'].__version__}) - Data manipulation ready")
    else:
        modules_check = False
    if modules["numpy"] is not None:
        print(f"[OK] numpy ({modules['numpy'].__version__}) - Numerical computation ready")
    else:
        modules_check = False
    if modules["requests"] is not None:
        print(f"[OK] requests ({modules['requests'].__version__}) - Network access ready")
    if modules["matplotlib"] is not None:
        print(f"[OK] matplotlib ({modules['matplotlib'].__version__}) - Visualization ready")
    else:
        modules_check = False
    if modules_check is True:
        print("Analyzing Matrix data...")
        intensity_data = modules["numpy"].random.normal(500, 50, 1000)
        data = {"intensity" : intensity_data}
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
        for key, value in modules.items():
            if value is None:
                print()
                print(f"[ERROR] {key} is missing")
                print("Install with pip:")
                print(f"pip install {key}")
                print()
                print("or install all dependencies:")
                print("pip install -r requirements.txt")


if __name__ == "__main__":
    main()
