from functools import wraps
from flask_jwt_extended import decode_token
from flask import request
from app.main.dataAccess import userDao

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            email=decode_token(token)["sub"]
            user=userDao.getByEmail(email)
            if user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        kwargs = user
        return f(*args, **kwargs)

    return decorated