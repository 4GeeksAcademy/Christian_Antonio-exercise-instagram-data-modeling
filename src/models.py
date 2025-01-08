import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(15), unique = True, nullable=False)
    firstname = Column(String(20), nullable = False)
    lastname = Column(String(20), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_from_id = relationship("user", backref="follower")
    user_to_id = relationship("user", backref="follower")

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = relationship("user", backref="post")

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, autoincrement=True, primary_key=True)
    type = Column(Enum('image', 'video', 'audio', name='media_types'))
    url = Column(String(200))
    post_id = relationship("post", backref= "media")

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, autoincrement=True, primary_key=True)
    comment_text = Column(String(200))
    author_id = relationship("user", backref="comment")
    post_id = relationship("post", backref="comment")
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
