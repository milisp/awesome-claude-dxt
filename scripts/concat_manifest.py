import json
from pathlib import Path

manifests = []

servers_dir = Path(__file__).parent.parent / "servers"
for owner in servers_dir.iterdir():
    if not owner.is_dir():
        continue
    for repo in owner.iterdir():
        if not repo.is_dir():
            continue
        manifest_path = repo / "manifest.json"
        if manifest_path.exists():
            try:
                with open(manifest_path) as f:
                    data = json.load(f)
                    data["tools"] = [
                        {"name": t["name"], "description": t.get("description", "")}
                        for t in data["tools"]
                    ]
                    data['prompts'] = []
                    manifests.append(data)
            except Exception as e:
                print(f"Error reading {manifest_path}: {e}")

output_path = Path(__file__).parent.parent / "manifests.json"
try:
    with open(output_path, "w") as f:
        json.dump(manifests, f, indent=2, ensure_ascii=False)
    print(f"Successfully merged {len(manifests)} manifests to {output_path}")
except Exception as e:
    print(f"Error writing output file: {e}")
