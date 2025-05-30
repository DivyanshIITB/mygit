def run(args):
    if args.b:
        print(f"Creating and switching to new branch: {args.branchName}")
    else:
        print(f"Switching to existing branch: {args.branchName}")