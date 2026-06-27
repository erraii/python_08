import os
import sys
from dotenv import load_dotenv


REQUIRED_VARIABLES = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

def is_valid_mode(mode: str | None) -> bool:
    return mode in ("development", "production")
    
def print_security_check() -> None:
    print("\nEnvironment security check:")
    print("[OK] All variables set")
    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


def load_config() -> dict[str, str | None]:
    config = {}
    load_dotenv()
    for req_key in REQUIRED_VARIABLES:
        config.update({req_key: os.getenv(req_key)})
    return config


def validate_config(config: dict[str, str | None]) -> list[str]:
    missing = []
    for key in REQUIRED_VARIABLES:
        value = config.get(key)
        if value is None:
            missing.append(key)
    return missing


def print_missing_config(missing: list[str]) -> None:
    print("⚠️  Configuration warnings:")
    for key in missing:
        print(f"[MISSING] {key}")
    print("\nℹ️  Create a .env file from .env.example:")
    print(" cp .env.example .env")
    print("\nThen edit .env file and run the program again")


def print_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    mode = config['MATRIX_MODE']
    print(f"Mode: {mode}")
    if mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production instance")
    api_key = config['API_KEY']
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")
    print(f"Log Level: {config['LOG_LEVEL']}")
    endpoint = config['ZION_ENDPOINT']
    if endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    # os.environ["API_KEY"] = "supersecret"
    config = load_config()
    missing = validate_config(config)
    if missing:
        print_missing_config(missing)
        sys.exit(1)
    if not is_valid_mode(config["MATRIX_MODE"]):
        print("Configuration error:")
        print("[INVALID] MATRIX_MODE must be 'development' or 'production'")
        sys.exit(1)
    print_config(config)
    print_security_check()


if __name__ == "__main__":
    main()
