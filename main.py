import argparse

import squares
import data
import calibration
import demo

def capture(args):
    squares.capture(args)

def supp(args):
    data.supp()

def info(args):
    data.info()

def process(args):
    parm = calibration.get_parameters()
    data.save_solution(parm)

def show_demo(args):
    demo.draw_coordinate(args)


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    capture_parser = subparsers.add_parser("capture")
    capture_parser.add_argument("--dt", help="time after which a successful attempt is saved and time between two attempts.", type=float, default=1)
    capture_parser.add_argument("--camera", help="camera id", type=int, default=0)
    capture_parser.add_argument("-x", help="Number of corner (x direction)", type=int, default=7)
    capture_parser.add_argument("-y", help="Number of corner (y direction)", type=int, default=7)
    capture_parser.set_defaults(func=capture)

    supp_parser = subparsers.add_parser("supp")
    supp_parser.set_defaults(func=supp)

    info_parser = subparsers.add_parser("info")
    info_parser.set_defaults(func=info)

    process_parser = subparsers.add_parser("process")
    process_parser.set_defaults(func=process)

    demo_parser = subparsers.add_parser("demo")
    demo_parser.set_defaults(func=show_demo)
    demo_parser.add_argument("--camera", help="camera id", type=int, default=0)
    demo_parser.add_argument("--x", help="Number of corner (x direction)", type=int, default=7)
    demo_parser.add_argument("--y", help="Number of corner (y direction)", type=int, default=7)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()