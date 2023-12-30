from rest_framework.exceptions import ValidationError


class UserDoesNotExist(ValidationError):
    def __init__(self, message="User does not exist!", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message or []
