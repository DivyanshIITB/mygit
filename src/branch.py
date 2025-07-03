import os

def run(args):
    refs_dir = ".mygit/refs/heads"
    head_file = ".mygit/HEAD"

    # Get current branch from HEAD
    current_branch = None
    if os.path.exists(head_file):
        with open(head_file, "r") as f:
            content = f.read().strip()
            if content.startswith("ref:"):
                current_branch = content[5:].strip().split('/')[-1]  # e.g., "refs/heads/dev" → "dev"

    print("[mygit] Branches:")
    if os.path.exists(refs_dir):
        for branch_name in sorted(os.listdir(refs_dir)):
            prefix = "*" if branch_name == current_branch else " "
            print(f" {prefix} {branch_name}")
