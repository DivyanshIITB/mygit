import argparse
import sys
from src import init, branch, add, commit, checkout, status, log

def main():
    parser = argparse.ArgumentParser(prog='mygit', description='Your own Git in Python!')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # `mygit init`
    init_parser = subparsers.add_parser('init', help='Initialize a new repository')
    init_parser.set_defaults(func=init.run)

    # mygit branch [branchName]
    branch_parser = subparsers.add_parser('branch', help='Create or list branches')
    branch_parser.add_argument('branchName', nargs='?', help='Name of the new branch (optional)')
    branch_parser.set_defaults(func=branch.run)

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

    # add log command
    log_parser = subparsers.add_parser('log', help='Show commit history')
    log_parser.set_defaults(func=log.run)

    # mygit status
    status_parser = subparsers.add_parser('status', help='Show working tree status')
    status_parser.set_defaults(func=status.run)

    args = parser.parse_args()
    args.func(args)  

if __name__ == '__main__':
    main()
