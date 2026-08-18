from app.services import *
from db.mysql_repository import *

services = Services()

tletters = {'b', 'a', 'd', 'e', 'g', 'h', 'n'}
treq = 'b'
tdate = dt.date.today()

PUZZ = Puzzle(letters = {'m', 'u', 'l', 't', 'i', 'v', 'e'}, required_let='m', puzzle_date=dt.date(year=2026, month=8, day=8))

def test_get_solutions():

    solutions = services.get_solutions(PUZZ)

    print(f"Found {len(solutions)} solutions")
    assert isinstance(solutions, list)
    # print(solutions)
    PUZZ.solutions.sort()
    new = sorted(PUZZ.solutions, key=len)
    assert isinstance(solutions[0], Word)
    assert PUZZ.required_let in solutions[10].letters

def test_save_puzzle():
    saved = services.save_user_puzzle(PUZZ)
    assert saved

def test_load_puzzle_history():
    history = services.load_puzzle_history()
    assert isinstance(history, list)
    print(len(history))

def test_create_puzzle():
    new_puzzle = services.create_puzzle(required_letter=treq, letters=tletters, puzz_date=tdate)
    assert isinstance(new_puzzle, Puzzle)
