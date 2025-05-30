import argparse
import sys
from core import init, add, commit, checkout

def main():
    parser = argparse.ArgumentParser(prog='mygit', description='Your own Git in Python!')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # `mygit init`
    init_parser = subparsers.add_parser('init', help='Initialize a new repository')
    init_parser.set_defaults(func=init.run)

    # `mygit add <file>`
    add_parser = subparsers.add_parser('add', help='Add file to staging area')
    add_parser.add_argument('filename')
    add_parser.set_defaults(func=add.run)

    # `mygit commit -m "message"`
    commit_parser = subparsers.add_parser('commit', help='Commit staged changes')
    commit_parser.add_argument('-m', '--message', required=True)
    commit_parser.set_defaults(func=commit.run)

    # subparser for checkout command
    checkoutParser = subparsers.add_parser("checkout")
    checkoutParser.add_argument("-b", action="store_true", help="Create a new branch")
    checkoutParser.add_argument("branchName")
    checkoutParser.set_defaults(func=checkout.run)

    args = parser.parse_args()
    args.func(args)  

if __name__ == '__main__':
    main()
