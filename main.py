import argparse

import squares

def capture(args):
    squares.capture(args)


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    capture_parser = subparsers.add_parser("capture")
    capture_parser.add_argument("--dt", help="tume between attempts", type=float, default=1)
    capture_parser.add_argument("--camera", help="camera id", type=int, default=0)
    capture_parser.add_argument("--x", help="Number of corner (x direction)", type=int, default=7)
    capture_parser.add_argument("--y", help="Number of corner (y direction)", type=int, default=7)

    capture_parser.set_defaults(func=capture)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()