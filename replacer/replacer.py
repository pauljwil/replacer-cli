import os
import re

def find(filename, old):
    """Find every instance of a given string in a particular file."""
    with open(filename, 'r', errors='ignore') as f:
        text = f.read()
        text = re.findall(old, text)
        num = len(text)
        return num

def find_iterator(dir, old):
    """Iterate through all the files in a directory, calling the find() function on each file."""
    found = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            filename = os.path.join(root, file)
            found += find(filename, old)
    print(f'Found {found} instances of "{old}" in this directory.')
    return found

def replace(filename, old, new):
    """Find and replace every instance of a given string in a particular file."""
    with open(filename, "r+", errors='ignore') as f:
        text = f.read()
        text = re.sub(old, new, text)
        f.truncate(0)
        f.seek(0)
        f.write(text)

def replace_iterator(dir, old, new):
    """Iterate through all the files in a directory, calling the replace() function on each file."""
    for root, dirs, files in os.walk(dir):
        for file in files:
            filename = os.path.join(root, file)
            replace(filename, old, new)
