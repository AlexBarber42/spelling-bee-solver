from db.mysql_repository import *

repo = MysqlRepository()
PUZZ = Puzzle(letters = {'m', 'u', 'l', 't', 'i', 'v', 'e'}, required_let='m')
PUZZ1 = Puzzle(letters = {'p', 'e', 'd', 'x', 'n', 'i', 'g'}, required_let='g', puzzle_date=dt.date(2026, 8, 7))
def test_load_lexicon():
    lexicon=repo.load_lexicon()

    assert lexicon.len==38277
    assert isinstance(lexicon,Lexicon)

def test_save_puzzle():
    x = repo.save_puzzle(PUZZ)
    print(x)

def test_get_history():
    y = repo.save_puzzle(PUZZ1)
    history = repo.get_puzzle_history()
    assert isinstance(history,list)
