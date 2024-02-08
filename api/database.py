import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# Each instance of the SessionLocal class will be a database session. The
# class itself is not a database session yet.We name it SessionLocal to
# distinguish it from the Session we are importing from SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We use the class returned by declarative_base() later to create each of the
# database models or classes (the ORM models).
Base = declarative_base()
