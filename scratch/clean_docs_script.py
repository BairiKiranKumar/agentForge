with open('scratch/write_root_docs.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace any literal \u2014 in the text
c = c.replace('\u2014', '')
with open('scratch/write_root_docs.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Cleaned scratch/write_root_docs.py")
