# from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
# from sqlalchemy.orm import relationship

# from database import Base, SessionLocal

# session = SessionLocal


# class AbstractBaseClass(Base):
#     __abstract__ = True
#     id = Column(Integer, primary_key=True, index=True)

#     @classmethod
#     async def count(cls, query=None, *args, **kwargs):
#         # import pdb;pdb.set_trace()
#         if not query:
#             return session.query(cls).count()
#         return query.count()

#     @classmethod
#     async def list(cls, query=None, *args, **kwargs):
#         if not query:
#             query = session.query(cls)
#         query = query.limit(kwargs.get('_limit')).offset(kwargs.get('_offset'))
#         return query


# class User(AbstractBaseClass):
#     __tablename__ = 'users'

#     email = Column(String(250), unique=True, index=True)
#     password = Column(String(250))
#     firstname = Column(String(250), nullable=True)
#     lastname = Column(String(250), nullable=True)
#     is_active = Column(Boolean, default=True)
#     token = Column(String(250), nullable=True)


# class Account(AbstractBaseClass):
#     __tablename__ = 'accounts'
#     account_name = Column(String(250), index=True)
#     account_number = Column(Integer, index=True, unique=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship(User, foreign_keys=[user_id], backref='accounts')
