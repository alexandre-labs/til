import datetime

from til.domain.learning import Learning
from .interfaces import Error, InvalidRequest, Success, UseCase, ValidRequest


class RegisterTILRequest(ValidRequest):
    def __init__(self, learning):
        self.learning = learning

    @classmethod
    def create(cls, title, description, timestamp):

        invalid_request = InvalidRequest()

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
    def execute(self, request):

        if not request:
            return Error.build_from_invalid_request(request)

        result = self.repository.save(request.learning)

        return Success(result=result)
