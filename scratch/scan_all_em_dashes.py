import os

em_dash = chr(8212)
bad_files = []

for root, dirs, files in os.walk('.'):
    # skip .git or scratch
    if '.git' in root or 'scratch' in root or '.claude' in root:
        continue
    for f in files:
        if f.endswith('.md') or f.endswith('.yaml') or f.endswith('.json'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fh:
                    content = fh.read()
                    if em_dash in content:
                        bad_files.append((path, content.count(em_dash)))
            except Exception as e:
                pass

if bad_files:
    print(f"Found {len(bad_files)} files with em dashes:")
    for p, c in bad_files:
        print(f"  {p}: {c}")
else:
    print("Zero em dashes found across all repository markdown, yaml, and json files!")
