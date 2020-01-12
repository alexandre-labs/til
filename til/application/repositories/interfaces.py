import abc


class LearningRepository(abc.ABC):

    @abc.abstractmethod
    def ping(self) -> bool:
        return NotImplemented

    @abc.abstractmethod
    def save(self, learning):
        return NotImplemented
