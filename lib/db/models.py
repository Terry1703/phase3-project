from sqlalchemy import column,Integer,string,ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__='users'
    
    id = column(Integer,primary_key=True)
    name =column(string,nullable = False)
    email =column(string,unique=True, nullable=False)
    
    class Post(Base):
        __tablename__= 'posts'
        
        id = column(Integer,primary_key=True)
        title = column(string,nullable=False)
        content =column(string,nullable=False)
        user_id = column(Integer,ForeignKey('users.id'))
        
        user = relationship('User', back_populates='posts')
        
User.posts = relationship('Post',back_populates='user')    
        
