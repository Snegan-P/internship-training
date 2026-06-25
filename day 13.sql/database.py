from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://postgres:Snegan%4026@localhost:5432/orm_database"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    bind=engine
)


Base = declarative_base()