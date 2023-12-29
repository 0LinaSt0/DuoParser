from utils.argparser import get_arguments
from scraper.words_scraper import WordsScraper


def lets_scrape():
    user_data_dir, \
    class_id, \
    attachment_name, \
    main_union_number, \
    level_name \
        = get_arguments()

    with WordsScraper(user_data_dir, class_id) as scraper:
        scraper.get_words()

        scraper.save_words_by_unit_to_json(main_union_number, attachment_name)

        scraper.save_words_by_level_to_json(level_name, attachment_name)



if __name__ == '__main__':
    lets_scrape()


