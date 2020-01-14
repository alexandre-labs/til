import abc
import typing as t


class InvalidRequest:

    errors: t.List[t.Dict[str, str]]

    def __init__(self) -> None:
        self.errors = []

    def __bool__(self) -> bool:
        return False

    def add_error(self, item: str, message: str) -> None:
        self.errors.append({item: message})


class ValidRequest(abc.ABC):
    def __bool__(self) -> bool:
        return True

    @abc.abstractclassmethod
    def create(self, **kwargs):
        return NotImplemented


class Response(abc.ABC):
    def __init__(self, result: t.Any):
        self.result = result

    @abc.abstractmethod
    def __bool__(self) -> bool:
        return NotImplemented


class Error(Response):
    def __bool__(self) -> bool:
        return False

    @classmethod
    def build_from_invalid_request(cls, invalid_request) -> "Error":
        return Error(result=invalid_request.errors)


class Success(Response):
    def __bool__(self) -> bool:
        return True


class UseCase(abc.ABC):
    def __init__(self, settings, repository=None):
        self.settings = settings
        self.repository = repository

    @abc.abstractmethod
    def execute(self, request):
        return NotImplemented
