import sys
sys.path.insert(0, 'scratch')
import write_root_docs as wrd

text = wrd.gaps_limitations_content
print("Total length:", len(text))
for i, line in enumerate(text.splitlines()):
    if '\u2014' in line:
        print(f"Line {i+1}: {repr(line)}")
