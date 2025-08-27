import argparse
from commands import add, list_cmd, delete, summary

def main():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    # list
    subparsers.add_parser("list")

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    # summary
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int, required=False)

    args = parser.parse_args()

    if args.command == "add":
        add.run(args.description, args.amount)
    elif args.command == "list":
        list_cmd.run()
    elif args.command == "delete":
        delete.run(args.id)
    elif args.command == "summary":
        summary.run(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
