from collections import Counter

from read_the_docs import word_counter, get_top_three


def test_word_counter():
    actual = word_counter()
    assert isinstance(actual, Counter)
    assert actual["is"] == 10
    assert actual["namespaces"] == 1


def test_get_top_three():
    assert get_top_three() == ["is", "better", "than"]