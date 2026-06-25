from database import engine
from database import SessionLocal

from database import Base

from models import User,Post



# create tables

Base.metadata.create_all(engine)


session = SessionLocal()

# CREATE USER

user1 = User(
    name="Snegan",
    email="snegan@gmail.com"
)

session.add(user1)

session.commit()

# CREATE POST

post1 = Post(
    title="Learning SQLAlchemy",
    user_id=user1.id
)

session.add(post1)

session.commit()


# READ USERS

users = session.query(User).all()

for user in users:

    print(
        user.id,
        user.name,
        user.email
    )


# FILTER

result = session.query(User).filter(
    User.name=="Snegan"
).first()


print(result.name)

# UPDATE

result.name="SNT"
session.commit()


# DELETE

delete_user = session.query(User).filter(
    User.id==1

).first()

if delete_user :

    session.delete(delete_user)
    session.commit()


# RELATIONSHIP QUERY


user = session.query(User).first()

if user:
    print(user.posts)
else:
    print("no users found")    

