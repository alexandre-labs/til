import abc


class LearningRepository(abc.ABC):

    def __init__(self, settings):
        self.settings = settings

    @abc.abstractmethod
    def save(self, learning):
        return NotImplemented
