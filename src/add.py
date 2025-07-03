import os
import hashlib

def hash_file_content(content):
    return hashlib.sha1(content).hexdigest()

def run(args):
    filename = args.filename

    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    with open(filename, 'rb') as f:
        content = f.read()

    sha1_hash = hash_file_content(content)
    obj_path = os.path.join('.mygit', 'objects', sha1_hash)

    # Save blob if not already stored
    if not os.path.exists(obj_path):
        with open(obj_path, 'wb') as f:
            f.write(content)

    # Update index
    with open('.mygit/index', 'a') as index:
        index.write(f"{sha1_hash} {filename}\n")

    print(f"Added {filename} to staging area.")
