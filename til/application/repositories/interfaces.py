import abc

from til.domain.learning import Learning


class LearningRepository(abc.ABC):
    def __init__(self, settings):
        self.settings = settings

    @abc.abstractmethod
    def save(self, learning: Learning):
        return NotImplemented
