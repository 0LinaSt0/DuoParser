import argparse

from typing import Dict, Tuple, Any


__all__ = ['get_arguments']


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


def get_arguments() -> Tuple[str, str, str, str]:
    '''
    Parse expected user_data_dir, class_id,
    attachment_name, main_union_number, level_name

    Returns
    -------
    Tuple[str, str, str, str]
        user_data_dir, class_id, attachment_name, main_union_number, level_name
    '''

    mandatory_confs = {
        'type':str,
        'required':True
    }

    optional_confs = {
        'nargs':'?',
        'const': None,
        'type': str
    }

    args = argparser(
        (
            ('-d', '--user_data_dir'),
            {**mandatory_confs, 'help': 'Path to User Data directory'}
        ),
        (
            ('-i', '--class_id'),
            {**mandatory_confs, 'help': 'Id number of class on Duolingo for school service'}
        ),
        (
            ('-n', '--attachment_name'),
            {**optional_confs, 'help': 'Attachment to output files'}
        ),
        (
            ('-u', '--main_union_number'),
            {**optional_confs, 'help': 'Number of interested unit'}
        ),
        (
            ('-l', '--level_name'),
            {**optional_confs, 'help': 'Name of interested level'}
        )
    )

    user_data_dir = args.user_data_dir
    class_id = args.class_id
    attachment_name = (args.attachment_name if args.attachment_name
                    else f'{class_id}_words.json')
    main_union_number = int(args.main_union_number if args.main_union_number
                            else 0)
    level_name = (args.level_name if args.level_name else '')

    return user_data_dir, class_id, attachment_name, main_union_number, level_name






