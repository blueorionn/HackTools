# Copyright (c) 2025-present, Swadhin
# This Python script generates a sequence of numbers
# within a user-specified range (start and end, inclusive).

import argparse
import pathlib
import sys


def generate_sequnce(start: int, end: int):
    if start > end:
        sys.stdout.write(f"Start index {end} is greater than End index {start} \n")
        sys.exit(1)

    return "\n".join([str(i) for i in range(start, (end + 1))])


# TODO: Support for float data type
# TODO: Rename file to generate_sequnce and add other sequence generator like alphabet generator etc.
def main():
    parser = argparse.ArgumentParser(
        prog="sequence_generator",
        description="Generate a sequence of numbers"
        + " within a user-specified range (start and end, inclusive).",
        epilog="Thanks for using %(prog)s! :)",
    )

    parser.add_argument("start", type=int, help="Start Index")
    parser.add_argument("end", type=int, help="End Index")
    parser.add_argument("-o", "--output-file", type=pathlib.Path, help="Output file")

    args = parser.parse_args()

    if (not args.output_file) and type(args.output_file) != str:
        sys.stdout.write(generate_sequnce(args.start, args.end))

    if type(args.output_file) == pathlib.PosixPath:
        if (str(args.output_file).split(".")[-1]) != "txt":
            sys.stdout.write("Invalid filetype only txt files are supported. \n")
            sys.exit(1)

        try:
            with open(str(args.output_file), "w+") as f:
                content = generate_sequnce(args.start, args.end)
                f.write(content)
                f.close()
        except Exception as e:
            sys.stdout.write(str(e) + "\n")
            sys.exit(1)


if __name__ == "__main__":
    main()
