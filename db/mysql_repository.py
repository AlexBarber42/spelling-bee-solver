from db.repository import *
from app.solver_info import *
import mysql.connector

class MysqlRepository(Repository):

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            #'host': 'db',
            #'port': '3306',
            'host': 'localhost', #run locally
            'port': '32000', # run locally
            'database': 'bee'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def load_lexicon(self):
        sql = "SELECT word FROM lexicon"
        self.cursor.execute(sql)
        result = {Word(word[0].rstrip('\n')) for word in self.cursor.fetchall()}
        return Lexicon(result)

    def save_puzzle(self, puzzle: Puzzle):
        sql = "INSERT INTO user_history(required_letter, letters, puzzle_date) VALUES (%s, %s, %s)"
        letters=list(puzzle.letters)
        let_string=''.join(letters)
        self.cursor.execute(sql, (puzzle.required_let, let_string, puzzle.date))
        self.connection.commit()
        sql = "SELECT puzzle_id from user_history where puzzle_date= (%s)"
        self.cursor.execute(sql, [puzzle.date])
        id = self.cursor.fetchone()
        return id

    def get_puzzle_history(self):
        sql = "SELECT letters, required_letter, puzzle_date from user_history "
        self.cursor.execute(sql)
        history = [puzzle for puzzle in self.cursor.fetchall()]
        return history
