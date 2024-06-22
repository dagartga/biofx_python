#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@DESKTOP-T859VC1>
Date   : 2024-06-20
Purpose: Calculate Fibonacci
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """Command-line arguments"""

    generations: int
    litter: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Calculate Fibonacci",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("generations", help="Number of generations")

    parser.add_argument("litter", help="Size of litter per generation")

    args = parser.parse_args()

    return Args(args.generations, args.litter)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()

    print(args.generations)
    print(args.litter)


# --------------------------------------------------
if __name__ == "__main__":
    main()
