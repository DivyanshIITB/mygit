import os

def run(args=None):
    if os.path.exists('.mygit'):
        print("Repository already initialized.")
        return

    os.makedirs('.mygit/objects', exist_ok=True)
    os.makedirs('.mygit/refs', exist_ok=True)

    with open('.mygit/index', 'w') as f:
        pass  # Empty index file

    print("Initialized empty mygit repository in .mygit/")
