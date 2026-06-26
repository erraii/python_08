import os
import sys
import site


def if_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct")

    print(f"\nCurrent Python: {sys.executable}")
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    site_packages = site.getsitepackages()
    print("\nPackage installation path:")
    print(site_packages[0])


def if_not_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in")

    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("\nThen run this program again.")


def check_if_venv() -> None:

    # METHOD number 1:
    # if sys.base_prefix != sys.prefix):

    # METHOD number 2:
    if 'VIRTUAL_ENV' in os.environ:
        if_venv()
    else:
        if_not_venv()


def main() -> None:
    check_if_venv()


if __name__ == "__main__":

    # to test, you can create a virtual environment:
    # virtualenv virtualenv_name

    # then activate it by:
    # source virtualenv_name/bin/activate

    # deactivate the virtual environment by:
    # deactivate
    main()
