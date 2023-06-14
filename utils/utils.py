import jwt
from app.models import User


class JWT:
    @staticmethod
    def encode(data):
        if not isinstance(data, dict):
            raise Exception("Data should be a dictionary")
        return jwt.encode(data, "abcd", algorithm="HS256")

    @staticmethod
    def decode(token):
        try:
            return jwt.decode(token, "abcd", algorithms=["HS256"])
        except jwt.exceptions.PyJWTError as e:
            raise e


def verify_superuser(function):
    def wrapper(request, *args, **kwargs):
        token = request.headers.get("token")
        if not token:
            raise Exception("Token not found")
        decoded = JWT().decode(token)
        user = User.objects.get(id=decoded.get("user_id"))
        if not user:
            raise Exception("Invalid user")
        if not user.is_superuser:
            raise Exception("User is unauthorized to perform the task")
        return function(request, *args, **kwargs)

    return wrapper
