import abc


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self):
        raise NotImplementedError

    @abc.abstractmethod
    def save_puzzle(self, puzzle):
        raise NotImplementedError

    @abc.abstractmethod
    def get_puzzle_history(self):
        raise NotImplementedError