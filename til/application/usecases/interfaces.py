import abc


# TODO: Add type hints
#
#
class UseCaseRequest(abc.ABC):

    @abc.abstractclassmethod
    def create(cls, **kwargs):
        return NotImplemented


class UseCaseResponse(abc.ABC):

    def __init__(self, value):
        self._value = value

    @abc.abstractproperty
    def result(self):
        return NotImplemented


class UseCase(abc.ABC):

    def __init__(self, settings, repository=None):
        self.settings = settings
        self.repository = repository

    @abc.abstractmethod
    def execute(self, request):
        return NotImplemented
