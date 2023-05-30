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
                "error": "Please login to your account.",
            }, 403
        try:
            email=decode_token(token)["sub"]
            user=userDao.getByEmail(email)
            if user is None:
                return {
                "error": "Invalid Authentication token!",
            }, 403
        except Exception as e:
            return {
                "error": "Invalid Authentication token!",
            }, 403
        kwargs = user
        return f(*args, **kwargs)

    return decorated