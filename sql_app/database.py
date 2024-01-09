from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgressserver:5432:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}
) #connect args is just for sqlite not for postgress

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
