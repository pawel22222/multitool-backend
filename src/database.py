from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import CONFIG

SQLALCHEMY_DATABASE_URL = f'{CONFIG.DB_DRIVER}://{CONFIG.DB_USER}:{CONFIG.DB_PASSWORD}@{CONFIG.DB_HOST}:{CONFIG.DB_PORT}/{CONFIG.DB_DATABASE}'

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
