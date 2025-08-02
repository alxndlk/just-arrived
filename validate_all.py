import json
import sys
from pathlib import Path
from pydantic import ValidationError
from city_schema import CityData, DevCityData

SKIP_DIRS = {"__pycache__", ".venv", "logs", "functions"}

def is_skipped(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)

def validate_json_file(path: Path) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            print(f"INVALID: {path}")
            print("Reason: Top-level JSON is not a dictionary.")
            return False

        env = data.get("_meta", {}).get("env", "development")
        SchemaClass = CityData if env == "production" else DevCityData

        SchemaClass(**data)
        print(f"✅ VALID ({env}): {path}")
        return True

    except (json.JSONDecodeError, ValidationError, TypeError) as e:
        print(f"❌ INVALID: {path}")
        print(f"Reason: {e}")
        return False

def main():
    json_files = [
        f for f in Path("en").rglob("*.json")
        if not is_skipped(f)
    ]

    if not json_files:
        print("⚠️ No JSON files found.")
        sys.exit(0)

    print(f"🔍 Validating {len(json_files)} files...\n")

    failed = 0
    for file in json_files:
        if not validate_json_file(file):
            failed += 1

    print(f"\n✅ Passed: {len(json_files) - failed}")
    print(f"❌ Failed: {failed}")

    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
