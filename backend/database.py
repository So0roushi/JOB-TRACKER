from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import os

db_url = os.getenv("DATABASE_URL", "sqlite:///./tracker.db")


class Base(DeclarativeBase):
    pass

engine = create_engine(db_url)

SessionLocal = sessionmaker(engine)

def get_db():
    with SessionLocal as session:
        try:
                yield session
                

        finally:
            session.close()


