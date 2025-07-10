import os
from pathlib import Path
import subprocess
import platform, time

servers_dir = Path(__file__).parent.parent / "servers"

def open_file_cross_platform(file_path):
    system = platform.system()

    if system == 'Darwin':  # macOS
        subprocess.run(['open', file_path])
    elif system == 'Windows':
        os.startfile(file_path)  # Windows only
    elif system == 'Linux':
        subprocess.run(['xdg-open', file_path])
    else:
        raise OSError(f"Unsupported OS: {system}")

def generate_dxt_and_maybe_open(repo_path):
    repo = Path(repo_path)

    origin_dxts = set(f.name for f in repo.glob("*.dxt"))
    if origin_dxts:
        new_file = repo / list(origin_dxts)[0]
        open_file_cross_platform(str(new_file))
        time.sleep(5)
    else:
        subprocess.run(["dxt", "pack"], cwd=repo, check=True)
        time.sleep(5)
        new_dxts = set(f.name for f in repo.glob("*.dxt"))

        if new_dxts:
            new_file = repo / list(new_dxts)[0]
            print(f"Opening new dxt file: {new_file}")
            open_file_cross_platform(str(new_file))
        else:
            print("No new .dxt file was created.")

for owner in servers_dir.iterdir():
    for repo in owner.iterdir():
        if repo.is_dir():
            manifest_path = repo / "manifest.json"
            if manifest_path.exists():
                try:
                    generate_dxt_and_maybe_open(repo)
                except Exception as e:
                    print(e)
