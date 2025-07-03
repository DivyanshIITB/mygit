import os
import hashlib
from datetime import datetime

INDEX_FILE = ".mygit/index"
OBJECTS_DIR = ".mygit/objects"
COMMITS_DIR = ".mygit/commits"
HEAD_FILE = ".mygit/HEAD"

def generate_hash(data):
    return hashlib.sha1(data.encode()).hexdigest()

def run(args):
    if not os.path.exists(INDEX_FILE):
        print("Nothing to commit. Staging area is empty.")
        return

    with open(INDEX_FILE, "r") as f:
        index_content = f.read()

    if not index_content.strip():
        print("Nothing to commit. Staging area is empty.")
        return

    # Prepare file map from index
    file_map = {}
    for line in index_content.strip().splitlines():
        blob_hash, filename = line.strip().split()
        file_map[filename] = blob_hash

    # Save each blob
    os.makedirs(OBJECTS_DIR, exist_ok=True)
    for filename, blob_hash in file_map.items():
        blob_path = os.path.join(OBJECTS_DIR, blob_hash)
        if not os.path.exists(blob_path):  # avoid duplicate saves
            with open(filename, "r") as f_src, open(blob_path, "w") as f_blob:
                f_blob.write(f_src.read())

    # Generate commit hash
    commit_data = "\n".join(f"{k} {v}" for k, v in file_map.items()) + args.message
    commit_hash = generate_hash(commit_data)

    # Read HEAD
    def get_head_commit():
        if not os.path.exists(HEAD_FILE):
            return ""

        with open(HEAD_FILE, "r") as f:
            content = f.read().strip()

        # Case 1: HEAD is pointing to a branch like "refs/heads/main"
        if content.startswith("refs/"):
            ref_path = os.path.join(".mygit", content)
            if os.path.exists(ref_path):
                with open(ref_path, "r") as ref_file:
                    return ref_file.read().strip()
            else:
                return ""

        # Case 2: HEAD contains a direct commit hash
        return content

    parent_hash = get_head_commit()

    # Write commit metadata
    os.makedirs(COMMITS_DIR, exist_ok=True)
    commit_path = os.path.join(COMMITS_DIR, commit_hash)
    with open(commit_path, "w") as f:
        f.write(f"commit_id: {commit_hash}\n")
        f.write(f"parent: {parent_hash}\n")
        f.write(f"timestamp: {datetime.now()}\n")
        f.write(f"message: {args.message}\n")
        f.write("files:\n")
        for filename, blob_hash in file_map.items():
            f.write(f"  {filename} {blob_hash}\n")

    # Update ref or HEAD
    with open(HEAD_FILE, "r") as f:
        head_content = f.read().strip()

    if head_content.startswith("ref:"):
        ref_path = os.path.join(".mygit", head_content[5:].strip())
        os.makedirs(os.path.dirname(ref_path), exist_ok=True)
        with open(ref_path, "w") as f:
            f.write(commit_hash)
    else:
        with open(HEAD_FILE, "w") as f:
            f.write(commit_hash)

    # Clear staging area
    with open(INDEX_FILE, "w") as f:
        f.write("")

    print(f"[mygit] Commit successful: {commit_hash}")
    