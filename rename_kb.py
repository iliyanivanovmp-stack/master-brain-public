import os
import re
import sys

def strip_uuid(filename):
    return re.sub(r' [a-f0-9]{32}(\.md)$', r'\1', filename)

def rename_dir(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for filename in filenames:
            if not filename.endswith('.md'):
                continue
            new_name = strip_uuid(filename)
            if new_name != filename:
                old = os.path.join(dirpath, filename)
                new = os.path.join(dirpath, new_name)
                if os.path.exists(new):
                    print(f"SKIP (exists): {new}")
                    continue
                os.rename(old, new)
                print(f"Renamed: {filename} → {new_name}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    rename_dir(target)
    print("Done.")
