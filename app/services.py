import db.mysql_repository
from app.solver_info import *

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def get_solutions(self, puzzle: Puzzle):
        lexicon =  self.repo.load_lexicon()
        solutions = [w for w in lexicon.lex if puzzle.required_let in w.letters and w.letters.issubset(puzzle.letters)]
        puzzle.solutions = [w.word for w in solutions]
        puzzle.pangrams = [w.word for w in solutions if w.letters == puzzle.letters]
        return solutions

    def save_user_puzzle(self, puzzle: Puzzle):
        return self.repo.save_puzzle(puzzle)


    def load_puzzle_history(self):
        return self.repo.get_puzzle_history()
