import argparse

from typing import Dict, Tuple, Any


def argparser(
    *args: Tuple[Tuple[str, str], Dict[str, Any]],
    description: str = None,
) -> argparse.Namespace:
    '''Parse coming arguments

    Parameters
    ----------
    *args : Tuple[Tuple[str, str], Dict[str, Any]]
        Expected arguments where:
            Tuple[str, str]     -> names of flags (short and long forms)
            Dict[atr, Any]      -> configurations of argument for using in
                                    parser.add_argument

    description : str, optional
        Description for argparser, by default None

    Returns
    -------
    argparse.Namespace
        The parsed arguments
    '''

    parser = argparse.ArgumentParser(description=description)

    for arg in args:
        parser.add_argument(*arg[0], **arg[1])

    return parser.parse_args()


from enum import Enum


class Elements(Enum):
    UNITS = 'section.KF0CX'
    U_HEADER = 'header._3LSiE > div._2Z-Z4'
    U_POINTS = 'div._2i_uN'
    BUTTON_SHOW_WORDS = 'div > button.kRgiM'
    WORDS = 'div > div._3ewMG > div._1dAI3 > div._3D4G0 > p._2HH61'



