from homework2.task01 import get_longest_diverse_words, get_rarest_char
from homework2.task01 import count_punctuation_chars, count_non_ascii_chars
from homework2.task01 import get_most_common_non_ascii_char

answer = ['unmi\\u00dfverst\\u00e4ndliche', 'unver\\u00e4u\\u00dferlichen,',
          'Wiederbelebungs\\u00fcbungen', 'r\\u00e9sistance-Bewegungen,',
          '\\u00bbWaldg\\u00e4nger\\u00ab', 'Br\\u00fcckenschl\\u00e4gen;',
          'Werkst\\u00e4ttenlandschaft', 'Souver\\u00e4nit\\u00e4tsan-',
          'Meinungs\\u00e4u\\u00dferung', 'D\\u00e4monenschw\\u00e4rme']
text = 'data.txt'


def test_long_words():
    assert get_longest_diverse_words(text) == answer


def test_rerest_char():
    assert get_rarest_char(text) == ")"


def test_count_punctuation_char():
    assert count_punctuation_chars(text) == 4132


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(text) == 2971


def test_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(text) == 'daß'