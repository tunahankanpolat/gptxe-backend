from functools import wraps
from flask_jwt_extended import decode_token
from flask import request
from app.main.dataAccess.userDao import getByEmail

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers.get("Authorization")
        if not token:
            return {
                "error": "Please login to your account.",
            }, 403
        try:
            email=decode_token(token).get("sub")
            user=getByEmail(email)
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