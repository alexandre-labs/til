import datetime
import typing as t

from til.domain.learning import Learning
from .interfaces import Error, InvalidRequest, Success, UseCase, ValidRequest


class RegisterTILRequest(ValidRequest):
    learning: Learning

    def __init__(self, learning) -> None:
        self.learning = learning

    @classmethod
    def create(cls, **kwargs):

        invalid_request = InvalidRequest()

        title = kwargs.get("title")
        description = kwargs.get("description")
        timestamp = kwargs.get("timestamp")

        if not isinstance(title, str):
            invalid_request.add_error("title", "Invalid title")

        if not isinstance(description, str):
            invalid_request.add_error("description", "Invalid title")

        if not isinstance(timestamp, datetime.date):
            invalid_request.add_error("timestamp", "Invalid timestamp")

        if invalid_request.errors:
            return invalid_request

        learning = Learning(title=title, description=description, timestamp=timestamp)

        return RegisterTILRequest(learning=learning)


class RegisterTIL(UseCase):
    def execute(
        self, request: t.Union[InvalidRequest, RegisterTILRequest]
    ) -> t.Union[Error, Success]:

        if not request:
            return Error.build_from_invalid_request(request)

        result = self.repository.save(request.learning)  # type: ignore

        return Success(result=result)
