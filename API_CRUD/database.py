# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.ext.declarative import declarative_base

# MYSQL_DB_URL = "mysql+mysqlconnector://root:root@localhost:3306/fastap_database"
# engine = create_engine(MYSQL_DB_URL)

# SessionLocal = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine))

# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

 