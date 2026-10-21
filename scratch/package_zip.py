import os
import shutil
import zipfile

target_zip = r"C:\Users\KiranKumar Bairi\.gemini\antigravity-ide\brain\1f8baaa0-5b45-45f3-a42c-27bb5d93eaec\scratch\ai-team-completed.zip"
source_dir = r"c:\Users\KiranKumar Bairi\Desktop\ai-team-snapshot\ai-team"

os.makedirs(os.path.dirname(target_zip), exist_ok=True)

print(f"Creating zip at: {target_zip}")

count = 0
with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(source_dir):
        # Exclude temporary scratch files, git, or temporary node/python caches if any
        if 'scratch' in root or '.git' in root or '__pycache__' in root:
            continue
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, source_dir)
            zf.write(full_path, os.path.join("ai-team", rel_path))
            count += 1

size_mb = os.path.getsize(target_zip) / (1024 * 1024)
print(f"Successfully packaged {count} files into {target_zip} ({size_mb:.2f} MB)")
