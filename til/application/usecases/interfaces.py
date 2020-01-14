import abc


# TODO: Add type hints
#
#
class InvalidRequest:
    def __init__(self):
        self.errors = []

    def __bool__(self):
        return False

    def add_error(self, item, message):
        self.errors.append({item: message})


class ValidRequest(abc.ABC):
    def __bool__(self):
        return True

    @abc.abstractclassmethod
    def create(self, **kwargs):
        return NotImplemented


class Response(abc.ABC):
    def __init__(self, result):
        self.result = result

    @abc.abstractmethod
    def __bool__(self):
        return NotImplemented


class Error(Response):
    def __bool__(self):
        return False

    @classmethod
    def build_from_invalid_request(cls, invalid_request):
        return Error(result=invalid_request.errors)


class Success(Response):
    def __bool__(self):
        return True


class UseCase(abc.ABC):
    def __init__(self, settings, repository=None):
        self.settings = settings
        self.repository = repository

    @abc.abstractmethod
    def execute(self, request):
        return NotImplemented
