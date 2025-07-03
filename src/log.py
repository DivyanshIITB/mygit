import os

HEAD_FILE = ".mygit/HEAD"
COMMITS_DIR = ".mygit/commits"

def run(args):
    # Step 1: Resolve HEAD to a commit hash
    if not os.path.exists(HEAD_FILE):
        print("[mygit] Repository not initialized.")
        return

    with open(HEAD_FILE, "r") as f:
        head = f.read().strip()

    # Handle symbolic ref (e.g., ref: refs/heads/main)
    if head.startswith("ref:"):
        ref_path = os.path.join(".mygit", head[5:].strip())
        if not os.path.exists(ref_path):
            print(f"[mygit] Branch ref does not exist: {ref_path}")
            return
        with open(ref_path, "r") as f:
            commit_hash = f.read().strip()
    else:
        commit_hash = head

    # Step 2: Traverse and print commit history
    while commit_hash:
        commit_file = os.path.join(COMMITS_DIR, commit_hash)
        if not os.path.exists(commit_file):
            print(f"[mygit] Commit not found: {commit_hash}")
            break

        with open(commit_file, "r") as f:
            lines = f.readlines()

        meta = {}
        for line in lines:
            if line.startswith("commit_id:"):
                meta["commit"] = line.split(":", 1)[1].strip()
            elif line.startswith("parent:"):
                meta["parent"] = line.split(":", 1)[1].strip()
            elif line.startswith("timestamp:"):
                meta["timestamp"] = line.split(":", 1)[1].strip()
            elif line.startswith("message:"):
                meta["message"] = line.split(":", 1)[1].strip()

        print(f"commit:   {meta.get('commit')}")
        print(f"message:  {meta.get('message')}")
        print(f"timestamp:{meta.get('timestamp')}")
        if meta.get("parent"):
            print(f"parent:   {meta.get('parent')}")
        print()

        # Step to next commit
        next_commit = meta.get("parent")
        if not next_commit or next_commit == commit_hash:
            break
        commit_hash = next_commit
