from utils.argparser import get_arguments
from parser.words_parser import WordsParser


def lets_scrape():
    user_data_dir, \
    class_id, \
    attachment_name, \
    main_union_number, \
    level_name \
        = get_arguments()

    with WordsParser(user_data_dir, class_id) as parser:
        parser.get_words()

        parser.save_words_by_unit_to_json(main_union_number, attachment_name)

        parser.save_words_by_level_to_json(level_name, attachment_name)


if __name__ == '__main__':
    lets_scrape()


