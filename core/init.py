import os

def run(args):
    if not os.path.exists('.mygit'):
        os.makedirs('.mygit/objects')
        os.makedirs('.mygit/refs')
        with open('.mygit/HEAD', 'w') as f:
            f.write('ref: refs/heads/master\n')
        print('Initialized empty mygit repository in .mygit/')
    else:
        print('Repository already initialized.')
