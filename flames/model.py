from sqlalchemy import Column, Integer, String
from database import Base

class FlamesResult(Base):
    __tablename__ = "flames_results"

    id = Column(Integer, primary_key=True, index=True)
    name1 = Column(String)
    name2 = Column(String)
    result = Column(String)