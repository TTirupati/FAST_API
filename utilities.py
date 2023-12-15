from functools import wraps

from fastapi import HTTPException

import models


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = kwargs.get('db')
        if not kwargs.get('token'):
            raise HTTPException(status_code=401, detail='Token is missing in the header')
        if session:
            db_user = session.query(models.User).filter(models.User.token == kwargs.get('token')).first()
            if not db_user:
                raise HTTPException(status_code=401, detail='Invalid token')
        else:
            raise HTTPException(status_code=404, detail='Data not found')

        return func(*args, **kwargs)

    return wrapper

