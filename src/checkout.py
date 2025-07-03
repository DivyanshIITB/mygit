import os

COMMITS_DIR = ".mygit/commits"
OBJECTS_DIR = ".mygit/objects"
HEAD_FILE = ".mygit/HEAD"

def restore_files(file_map):
    for filename, blob_hash in file_map.items():
        blob_path = os.path.join(OBJECTS_DIR, blob_hash)
        if not os.path.exists(blob_path):
            print(f"[mygit] Error: Blob not found for {filename}")
            continue

        with open(blob_path, 'r') as f_blob:
            content = f_blob.read()

        with open(filename, 'w') as f_out:
            f_out.write(content)

        print(f"[mygit] Restored {filename}")

def run(args):
    if args.b:
        print("[mygit] Branch checkout with -b not implemented yet.")
        return

    branch_name = args.branchName
    branch_ref_path = os.path.join(".mygit", "refs", "heads", branch_name)

    # ✅ If it's a branch, read its commit hash
    if os.path.exists(branch_ref_path):
        with open(branch_ref_path, "r") as f:
            commit_id = f.read().strip()

        # ✅ Set HEAD to point to this branch
        with open(HEAD_FILE, "w") as f:
            f.write(f"ref: refs/heads/{branch_name}")
    else:
        print(f"[mygit] Error: Branch '{branch_name}' not found.")
        return

    # ✅ Now load and restore files from commit
    commit_path = os.path.join(COMMITS_DIR, commit_id)
    if not os.path.exists(commit_path):
        print(f"[mygit] Error: Commit {commit_id} does not exist.")
        return

    file_map = {}
    with open(commit_path, 'r') as f:
        lines = f.readlines()

    files_section = False
    for line in lines:
        line = line.strip()
        if line == "files:":
            files_section = True
            continue
        if files_section and line:
            parts = line.split()
            if len(parts) == 2:
                filename, blob_hash = parts
                file_map[filename] = blob_hash

    restore_files(file_map)
    print(f"[mygit] Switched to branch: {branch_name}")
