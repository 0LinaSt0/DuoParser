import re

import json

from sortedcontainers import SortedSet


def save_to_json(saved):
    with open('tmp.json', 'w', encoding='utf-8') as f:
        json.dump(saved, f, ensure_ascii=False)


def check_unstandart(units: dict) -> None:
    strange = {}
    pattern = r"^(?=.*[^A-Za-zÀ-ÿ\s]).+$"

    for key, unit in units.items():
        if unit[1]:
            strange_words = [word for word in unit[2] if bool(re.match(pattern, word))]
            if len(strange_words):
                strange[key] = strange_words

    save_to_json(strange)



def pars_by_words(units: dict, level_name: str):
    words = SortedSet()

    for unit in units.values():
        if unit[0] == level_name:
            words.update(unit[2])

    words = list(words)

    save_to_json(words)


def pars_by_unit(units: dict, n_unit: int):
    words = SortedSet()

    for key, value in units.items():
        if int(key) > n_unit:
            break
        words.update(value[2])

    words = list(words)
    save_to_json(words)


if __name__ == '__main__':

    # p = 'data/words/6731731_words.json'
    p = 'data/all_words.json'

    with open(p, 'r', encoding='utf-8') as file:
        units = json.load(file)

    # print(units)

    # pars_by_words(units, 'B2')
    pars_by_unit(units, 37)






