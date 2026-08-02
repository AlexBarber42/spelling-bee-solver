import abc


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self):
        raise NotImplementedError