# src/status.py

import os

INDEX_FILE = ".mygit/index"

def run(args):
    if not os.path.exists(INDEX_FILE):
        print("[mygit] No staging area found. Run `mygit init` first.")
        return

    with open(INDEX_FILE, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        print("[mygit] No files staged. Working directory clean.")
    else:
        print("[mygit] Files staged for commit:")
        for line in lines:
            # Only print the filename part
            parts = line.strip().split(maxsplit=1)
            filename = parts[1] if len(parts) > 1 else parts[0]
            print(f" - {filename}")
