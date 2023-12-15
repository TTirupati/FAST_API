from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
# from sqlalchemy.orm import relationship

from database import Base
class AbstractBaseClass(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)

class User(AbstractBaseClass):
    __tablename__ = 'users'

    email = Column(String(250), unique=True, index=True)
    password = Column(String(250))
    firstname = Column(String(250), nullable=True)
    lastname = Column(String(250), nullable=True)
    is_active = Column(Boolean, default=True)
    token = Column(String(250), nullable=True)
    


 
