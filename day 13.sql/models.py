from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from database import Base



class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True
    )


    name = Column(
        String(50),
        nullable=False
    )


    email = Column(
        String(100),
        unique=True
    )


    posts = relationship(
        "Post",
        back_populates="user"
    )




class Post(Base):

    __tablename__ = "posts"


    id = Column(
        Integer,
        primary_key=True
    )


    title = Column(
        String(100)
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    user = relationship(
        "User",
        back_populates="posts"
    )