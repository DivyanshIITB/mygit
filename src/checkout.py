import os

COMMITS_DIR = ".mygit/commits"
OBJECTS_DIR = ".mygit/objects"
HEAD_FILE = ".mygit/HEAD"
REFS_DIR = ".mygit/refs/heads"

def run(args):
    if args.b:
        # Create a new branch
        new_branch = args.branchName
        new_branch_path = os.path.join(REFS_DIR, new_branch)

        if os.path.exists(new_branch_path):
            print(f"[mygit] Error: Branch '{new_branch}' already exists.")
            return

        # Get current HEAD commit hash
        if not os.path.exists(HEAD_FILE):
            print("[mygit] Error: HEAD file not found.")
            return

        with open(HEAD_FILE, 'r') as f:
            head_content = f.read().strip()
            if head_content.startswith("ref:"):
                ref_path = os.path.join(".mygit", head_content[5:].strip())
                if os.path.exists(ref_path):
                    with open(ref_path, 'r') as rf:
                        commit_hash = rf.read().strip()
                else:
                    commit_hash = ""
            else:
                commit_hash = head_content

        # Create branch file and write commit hash
        os.makedirs(REFS_DIR, exist_ok=True)
        with open(new_branch_path, 'w') as f:
            f.write(commit_hash)

        # Point HEAD to new branch
        with open(HEAD_FILE, 'w') as f:
            f.write(f"ref: refs/heads/{new_branch}")

        print(f"[mygit] Created and switched to new branch: {new_branch}")
        return

    # ----------- Existing logic for checking out a commit/branch ------------
    branch_name = args.branchName
    branch_ref = os.path.join(REFS_DIR, branch_name)

    if os.path.exists(branch_ref):
        with open(branch_ref, 'r') as f:
            commit_id = f.read().strip()

        # Update HEAD to point to branch
        with open(HEAD_FILE, 'w') as f:
            f.write(f"ref: refs/heads/{branch_name}")

        # Restore files from commit
        restore_commit(commit_id)
        print(f"[mygit] Switched to branch: {branch_name}")
        return

    # If not a branch, try commit hash directly
    commit_id = branch_name
    commit_path = os.path.join(COMMITS_DIR, commit_id)
    if not os.path.exists(commit_path):
        print(f"[mygit] Error: Commit {commit_id} does not exist.")
        return

    restore_commit(commit_id)

    with open(HEAD_FILE, 'w') as f:
        f.write(commit_id)

    print(f"[mygit] Checked out commit: {commit_id}")


def restore_commit(commit_id):
    file_map = {}
    commit_path = os.path.join(COMMITS_DIR, commit_id)
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
