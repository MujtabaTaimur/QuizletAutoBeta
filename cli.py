import argparse
import getpass
from .runner import run_bot

def main():
    parser = argparse.ArgumentParser(description="Quizlet AutoBot")
    parser.add_argument("--set", help="Single Quizlet set URL")
    parser.add_argument("--set-file", help="File with multiple Quizlet set URLs")
    parser.add_argument("--modes", default="all", help="Modes: all or comma-separated list")
    parser.add_argument("--headless", action="store_true", help="Run browser headless")
    args = parser.parse_args()

    if not args.set and not args.set_file:
        print("Provide --set or --set-file")
        return 1

    username = input("Enter Quizlet username/email: ").strip()
    password = getpass.getpass("Enter Quizlet password: ")

    sets = []
    if args.set:
        sets.append(args.set.strip())
    if args.set_file:
        with open(args.set_file) as f:
            sets += [line.strip() for line in f if line.strip()]

    run_bot(username, password, sets, args.modes.split(",") if args.modes != "all" else "all", args.headless)
    return 0
