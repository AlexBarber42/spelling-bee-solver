from db.mysql_repository import *


repo = MysqlRepository()

def test_load_lexicon():
    lexicon=repo.load_lexicon()

    assert lexicon.len==38328
    assert isinstance(lexicon,Lexicon)
