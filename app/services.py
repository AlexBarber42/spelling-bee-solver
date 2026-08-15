import db.mysql_repository
from model.solver_info import *

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def create_puzzle(self, required_letter, letters, puzz_date):
        return Puzzle(required_let=required_letter, letters=letters, puzzle_date=puzz_date)

    def get_solutions(self, puzzle: Puzzle):
        lexicon =  self.repo.load_lexicon()
        solutions = [w for w in lexicon.lex if puzzle.required_let in w.letters and w.letters.issubset(puzzle.letters)]
        puzzle.solutions = [w.word for w in solutions]
        puzzle.pangrams = [w.word for w in solutions if w.letters == puzzle.letters]
        save = self.save_user_puzzle(puzzle)
        sols = {}
        for word in solutions:
            if word.length not in sols:
                sols[word.length] = []
            sols[word.length].append(word.word)
        sols[1] = {"Pangrams: ": puzzle.pangrams, "Puzzle Date: ": puzzle.date}
        return sols
    def save_user_puzzle(self, puzzle: Puzzle):
        return self.repo.save_puzzle(puzzle)


    def load_puzzle_history(self):
        return self.repo.get_puzzle_history()
