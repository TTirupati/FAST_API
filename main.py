import uuid
from fastapi import FastAPI ,Body,Depends,Header,HTTPException
from pydantic import BaseModel 
from uuid import UUID 
from datetime import datetime,time,timedelta
from database import engine,get_db
import models,schema
from sqlalchemy.orm import Session
from utilities import auth_required
 

app=FastAPI()

models.Base.metadata.create_all(bind=engine) #it will create the models like django migrate but it not upate or alter
 
@app.post('/login')
def login(user: schema.UserCreate, db: Session = Depends(get_db)):
    if user.email and user.password:
        db_user = db.query(models.User).filter(
            models.User.email == user.email,
            models.User.password == user.password
        ).first()
        if db_user:
            db_user.token = str(uuid.uuid4())
            db.commit()
            db.refresh(db_user)
            return {'message': 'Login Success', "token": db_user.token}
        else:
            raise HTTPException(status_code=401, detail='Invalid Credentials')
    raise HTTPException(status_code=404, detail="Data not found")


# User CRUD operations
@app.get('/users')
@auth_required
def get_users(db: Session = Depends(get_db), token: str = Header(None)):
    users = db.query(models.User).all()
    result = []
    for user in users:
        data = {'id': user.id, 'email': user.email, 'is_active': user.is_active,
                'firstname': user.firstname, 'lastname': user.lastname
                }
        result.append(data)
    return result


@app.post('/users', response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    #import pdb;pdb.set_trace()
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.put('/users/{user_id}', response_model=schema.User)
def update_user(user: schema.UserUpdate, user_id: int = None, db: Session = Depends(get_db)):
    if user_id:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail='User not found')
        db_user.firstname = user.firstname
        db_user.lastname = user.lastname
        db.commit()
        db.refresh(db_user)
        return db_user


@app.delete('/users/{user_id}')
def delete_user(user_id: int = None, db: Session = Depends(get_db)):
    if user_id:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail='User not found')
        db.delete(db_user)
        db.commit()
        return {'message': f'User of id {user_id} deleted successfully'}






# # Account CRUD operations
# @app.get('/accounts/')
# async def get_accounts(pagination: Pagination = Depends(),
#                        db: Session = Depends(get_db),
#                        query_params: schema.AccountParams = Depends()):
#     query_params = query_params.__dict__
#     filter_kwargs = {
#         key: value for key, value in query_params.items() if value is not None}
#     if not filter_kwargs:
#         query = db.query(models.Account)
#     else:
#         query = db.query(models.Account).filter_by(**filter_kwargs)

#     return await pagination.paginate(
#         serializer_class=serializers.AccountSerializer, query=query
#     )


# @app.get('/accounts/user-detail/')
# def get_accounts(db: Session = Depends(get_db)):
#     accounts = db.query(models.Account).all()
#     result = []
#     for account in accounts:
#         data = dict(
#             id=account.id,
#             accountName=account.account_name,
#             accountNumber=account.account_number,
#             userId=account.user_id,
#             user=dict(email=account.user.email, is_active=account.user.is_active) if account.user else None)
#         result.append(data)
#     return result


# @app.post('/accounts')
# def create_account(account: schema.CreateOrUpdateAccount, db: Session = Depends(get_db)):
#     db_account = models.Account(**account.dict())
#     db.add(db_account)
#     db.commit()
#     db.refresh(db_account)
#     return db_account


# @app.put('/accounts/{account_id}', response_model=schema.Account)
# def update_account(account: schema.CreateOrUpdateAccount, account_id: int = None, db: Session = Depends(get_db)):
#     if account_id:
#         db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
#         if not db_account:
#             raise HTTPException(status_code=404, detail='Account details not found')
#         db_account.account_name = account.account_name
#         db_account.lastname = account.account_number
#         db_account.user_id = account.user_id
#         db.commit()
#         db.refresh(db_account)
#         return db_account


# @app.delete('/accounts/{account_id}')
# def delete_account(account_id: int = None, db: Session = Depends(get_db)):
#     if account_id:
#         db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
#         if not db_account:
#             raise HTTPException(status_code=404, detail='User not found')
#         db.delete(db_account)
#         db.commit()
#         return {'message': f'Account of id {account_id} deleted successfully'}


