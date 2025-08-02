import json
import os

ROOT_DIR = "./en"  
entries = []

for file_name in os.listdir(ROOT_DIR):
    if not file_name.endswith(".json"):
        continue

    path = os.path.join(ROOT_DIR, file_name)
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            entries.append({
                "city": data.get("city_name", "").lower(),
                "country": data.get("country_code", "").upper(),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "file": f"en/{file_name}",
                "population": data.get("population", 0)
            })
        except Exception as e:
            print(f"❌ Failed on {file_name}: {e}")

with open("cities_index.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"✅ Generated cities_index.json with {len(entries)} entries")
