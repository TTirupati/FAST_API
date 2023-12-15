from pydantic import BaseModel


class AccountBase(BaseModel):
    account_name: str = None
    account_number: int = None
    user_id: int


class CreateOrUpdateAccount(AccountBase):
    pass


class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True


# orm_mode will tell the Pydantic model to read the data even if it is not a dict , but an ORM model


class UserCreate(BaseModel):
    email: str
    password: str
     


class UserUpdate(BaseModel):
    firstname: str = None
    lastname: str = None


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    firstname: str|None=None
    lastname: str |None=None

    class Config:
        orm_mode = True


class AccountParams:
    def __init__(
            self,
            account_name: str = None,
            account_number: int = None
    ):
        self.account_name = account_name
        self.account_number = account_number


"""
root--prokect:
    Base--DB,Abstrac..main.py
    App
     Models
       fatur1
         models
           url
"""
