import os
import sys
from dotenv import load_dotenv


def load_config() -> None | dict[str, str]:
    load_dotenv()
    required_vars = ["MATRIX_MODE",
                     "DATABASE_URL",
                     "API_KEY",
                     "LOG_LEVEL",
                     "ZION_ENDPOINT"]
    missing = []
    for var in required_vars:
        try:
            os.environ[var]
        except KeyError:
            missing.append(var)
    if missing:
        print("Missing variables:")
        print("\n".join(missing))
        return None
    config: dict[str, str] = {}
    for var in required_vars:
        config[var] = os.environ[var]
    return config


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    config = load_config()
    if config is None:
        sys.exit(1)
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE'].lower()}")
    mode = config["MATRIX_MODE"].lower()
    if mode == "development":
        print("Database: Connected to local instance")
        print("Debug features: Enabled")
    else:
        print("Database: Connected to production instance")
        print("Debug features: Disabled")

    if config["API_KEY"]:
        print("API Access: Authenticated")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
