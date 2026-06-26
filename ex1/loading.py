import importlib


PACKAGES = {
            "pandas": "2.1.0",
            "numpy": "1.25.0",
            "matplotlib": "3.7.2"
            }

DESCRIPTIONS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


def get_module_version(module_name: str) -> str | None:
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return None

    for attr in ("__version__", "VERSION", "version"):
        value = getattr(module, attr, None)

        if value is not None:
            return str(value)

    return None


def check_requirements() -> None:
    missing = []
    mismatched = []

    for package_name, req_version in PACKAGES.items():

        # Get installed version
        installed_version = get_module_version(package_name)
        if not installed_version:
            missing.append(package_name)
            continue

        # Check if installed version satisfies the specifier
        if installed_version not in req_version:
            mismatched.append({
                "package": package_name,
                "required": str(req_version),
                "installed": installed_version
                })

    # Report Results
    if missing:
        print("❌ Missing Dependencies:")
        for pkg in missing:
            print(f"  - {pkg}")

    if mismatched:
        print("\n⚠️ Version Mismatches:")
        for item in mismatched:
            print(f"  - {item['package']}: Required {item['required']}, Found {item['installed']}")

    if not missing and not mismatched:
        print("✅ All dependencies are satisfied.")


def main() -> None:
    check_requirements()


if __name__ == "__main__":
    main()
