from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./harrydave.db'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/harryapp'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

Base = declarative_base()


def connection():
    db = SessionLocal()
    try:
        # yield db
        return db  # Return the database session object
    finally:
        db.close()

# alembic revision --autogenerate
# alembic upgrade head