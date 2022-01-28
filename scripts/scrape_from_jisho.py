from typing import Tuple, List

from jisho_api.kanji import Kanji
from jisho_api.kanji.cfg import MainReadings
from jisho_api.sentence import Sentence

from jisho_api.word import Word
from jisho_api.cli import scrape

# word_requests = scrape(Kanji, ['角'], '~/japanese/test')


# print(word_requests)

def main_reading_to_str(main_reading: MainReadings) -> str:
    return ", ".join(main_reading.kun) + "; " + ", ".join(main_reading.on)


def get_main_meanings_and_readings(kanji: str) -> Tuple[str, str]:
    r = Kanji.request(kanji)
    return ", ".join(r.data.main_meanings), main_reading_to_str(r.data.main_readings)


# r = get_main_meanings_and_readings('年賀状')
# print(r)

r = Word.request('"角"')
print(r)
