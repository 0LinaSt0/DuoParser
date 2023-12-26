import argparse

from typing import List


def argparser(
    arg_name: str, description: str = None, help: str = None
) -> argparse.Namespace:

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(arg_name, type=str, help=help)

    return parser.parse_args()
