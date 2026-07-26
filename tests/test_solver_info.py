from app.solver_info import *
import pytest

def test_puzzle():
    date1 = dt.date(2026, 7, 19)

    puzzle2 = Puzzle(letters={'m', 'N', 'l', 'o', 'T', 'h'}, required_let='I')
    assert puzzle2.date == dt.date.today()
    assert len(puzzle2.letters) == 7
    assert puzzle2.letters == {'m', 'n', 'l', 'o', 't', 'h', 'i'}
    assert puzzle2.required_let == 'i'


def test_word():
    w1 = Word("test")
    assert w1.word == "test"
    assert w1.length == len("test")
    assert w1.letters == {"t", "s", "e"}

def test_lexicon():
    test_words={'test', 'words', 'set'}
    lex1=Lexicon(test_words)
    assert lex1.lex == test_words

