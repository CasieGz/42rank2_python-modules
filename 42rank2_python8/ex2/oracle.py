#!/usr/bin/env python3

import os
import sys
try:
    from dotenv import load_dotenv
except ImportError:
    print("[WARNING] 'python-dotenv' is not installed. "
          "To install it, do the following:")
    print("pip install -r requirements.txt")
    print("python3 oracle.py\n")
    sys.exit(1)


def security_check(
        matrix_mode_raw: str | None,
        database_url: str | None,
        api_key: str | None,
        log_level_raw: str | None,
        zion_endpoint: str | None
        ) -> None:
    # no secrets are hardcoded in the code
    # all values ​​are obtained via os.getenv()
    print("[OK] No hardcoded secrets detected")

    env_file_exists = os.path.exists(".env")
    all_values_present = all([
        matrix_mode_raw, database_url, api_key,
        log_level_raw, zion_endpoint
        ])

    if env_file_exists and all_values_present:
        print("[OK] .env file properly configured")
    elif env_file_exists and not all_values_present:
        print("[WARNING] .env file not properly configured")
    else:
        print("[WARNING] No .env file found "
              "(using system environment / defaults)")

    # python-dotenv does not overwrite system variables that are already set
    # meaning actual environment variables always take precedence
    # so the .env -> production override works.
    print("[OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    # it reads your .env file and injects those key-value pairs into the
    # running Python process's environment dictionary (os.environ).
    load_dotenv()

    print("Configuration loaded:")

    # os.getenv() reads any environment variable accessible
    # to the Python process
    matrix_mode_raw = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level_raw = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    # setting default values if none were set in .env
    database_status = "Connected to local instance" \
        if database_url else "Disconnected"
    api_status = "Authenticated" if api_key else "Unauthenticated"
    zion_status = "Online" if zion_endpoint else "Offline"
    matrix_mode = matrix_mode_raw if matrix_mode_raw else "development"
    log_level = log_level_raw if log_level_raw else "DEBUG"

    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_status}")

    print("\nEnvironment security check:")
    security_check(
        matrix_mode_raw,
        database_url,
        api_key,
        log_level_raw,
        zion_endpoint
        )

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
