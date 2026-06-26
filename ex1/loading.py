import importlib
import importlib.util


PACKAGES = {
            "pandas": "2.1.0",
            "numpy": "1.25.0",
            "matplotlib": "3.7.2"
            }

DESCRIPTIONS = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization"
}


def matrix_analysis() -> None:

    print("\nAnalyzing Matrix data...")
    numpy = importlib.import_module("numpy")
    pandas = importlib.import_module("pandas")
    pyplot = importlib.import_module("matplotlib.pyplot")

    # Set seed for reproducibility
    # numpy.random.seed(42)

    # Generate 1000 random x coordinates
    x_coordinates = numpy.random.random(1000)
    # Generate 1000 random y coordinates
    y_coordinates = numpy.random.random(1000)
    df = pandas.DataFrame()
    df['x'] = x_coordinates
    df['y'] = y_coordinates

    print("Processing 1000 data points...")
    # Average point
    mean_x = df["x"].mean()
    mean_y = df["y"].mean()

    # Distance to average point
    df["distance"] = numpy.sqrt(
        (df["x"] - mean_x) ** 2 + (df["y"] - mean_y) ** 2
    )

    # Poins inside distance 0.42
    inside = df["distance"] <= 0.42
    outside = df["distance"] > 0.42

    print("Generating visualization...")
    pyplot.title("Matrix Point Analysis")
    pyplot.xlabel("Position X")
    pyplot.ylabel("Position Y")

    # Points inside are blue
    pyplot.scatter(
        df.loc[inside, "x"],
        df.loc[inside, "y"],
        color="blue",
        marker="o",
        label="Distance <= 0.42"
    )

    # Points outside are red
    pyplot.scatter(
        df.loc[outside, "x"],
        df.loc[outside, "y"],
        color="red",
        marker="o",
        label="Distance > 0.42"
    )

    # Show average point
    pyplot.scatter(
        mean_x,
        mean_y,
        color="green",
        marker="x",
        s=100,
        label="Mean point"
    )

    pyplot.legend()
    pyplot.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def print_instrucions() -> None:

    print("\n❌ Missing dependencies detected!")
    print("\nTo install with pip, use:")
    print(" pip install -r requirements.txt")
    # print("\n  or use:")
    # for item in missing:
    #    print(f" pip install {item['package']}=={item['required']}")
    print("\nTo install with Poetry, use:")
    # for item in missing:
    #     print(f" poetry add {item['package']}=={item['required']}")
    print(" poetry install")


def get_module_version(module_name: str) -> str | None:

    spec = importlib.util.find_spec(module_name)

    if spec is None:
        return None

    try:
        module = importlib.import_module(module_name)
    except Exception:
        return "installed, but broken"

    for attr in ("__version__", "VERSION", "version"):
        value = getattr(module, attr, None)

        if value is not None:
            return str(value)

    return "installed, but version unknown"


def check_requirements() -> None:

    print("Checking dependencies:")
    missing = []

    for package_name, req_version in PACKAGES.items():

        # Get installed version
        installed_version = get_module_version(package_name)
        description = DESCRIPTIONS.get(package_name)
        # Check if installed
        if not installed_version:
            missing.append({
                "package": package_name,
                "required": str(req_version),
                "installed": installed_version
                })
            print(
                f"[MISSING] {package_name} {req_version} - "
                f"{description} missing"
                )
            continue

        # Check if installed version satisfies the specifier
        if installed_version not in req_version:
            missing.append({
                "package": package_name,
                "required": str(req_version),
                "installed": installed_version
                })
            print(
                f"[MISMATCH] {package_name} {installed_version} - "
                f"{description} mismatch, required: {req_version}"
                )
            continue

        print(f"[OK] {package_name} {installed_version} - {description} ready")

    # Report Results
    if missing:
        print_instrucions()

    else:
        # print("✅ All dependencies are satisfied.")
        matrix_analysis()


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    check_requirements()


if __name__ == "__main__":
    main()
