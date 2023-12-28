import re

from typing import List


def split_to_words(splitted_str: str) -> List[str]:
    '''
    Pattern: x(?!y) where x=',\s' and y=[^chars]*[chars]
    -------------------
    ,\s                         - split on ', '
    (?!                         - if after there are not
        [^\(\[\{] like [^([{]*  - any count of characters except '(', '[' or '{'
        [\)\]\}] like [)]}]     - ended on ')', ']' or '}'
    )
    '''

    pattern = r',\s(?![^/(/[/{]*[\)\]\}])'

    return re.split(pattern, splitted_str)
