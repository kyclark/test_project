#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2024-07-31
Purpose: Rock the Casbah
"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """Command-line arguments"""

    name: str
    age: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("name", metavar="NAME", help="Your name")

    parser.add_argument(
        "-a", "--age", help="Your age", metavar="INT", type=int, default=0
    )

    args = parser.parse_args()

    return Args(name=args.name, age=args.age)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    print(f"In ten years, you will be {add10(args.age)} years old!")


# --------------------------------------------------
def add10(val: int) -> int:
    """Add 10 to the value"""

    return val + 10


# --------------------------------------------------
def test_add10() -> None:
    """ Test add10 """

    assert add10(0) == 10
    assert add10(10) == 20


# --------------------------------------------------
if __name__ == "__main__":
    main()
