import datetime as dt

class Puzzle:
    def __init__(self, letters: set, required_let: str, puzzle_date : dt.date = dt.date.today()):

        self.required_let = required_let.casefold()
        self.date = puzzle_date
        self.letters = {letter.casefold() for letter in letters}
        self.solutions = []
        self.pangrams = []

    def __str__(self):
        return f"Letters = {self.letters}\nDate = {self.date}\nRequired letter = {self.required_let}\nPangrams = {self.pangrams}"

class Word:
    def __init__(self, word:str):
        self.word = word.casefold()
        self.length=len(self.word)
        self.letters= {letter for letter in self.word}

    def __str__(self):
        return f"Word = {self.word}\nLength = {self.length}\nLetters = {self.letters}"

class Lexicon:
    def __init__(self, words: set):
        self.lex = words
        self.len = len(self.lex)


