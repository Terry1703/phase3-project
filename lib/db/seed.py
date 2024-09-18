from models import User,Base,Post
from faker import Faker
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine

#setup database

engine = create_engine('squlite:///your_database_name.db')
session = sessionmaker(bind=engine)
session = session()

#initialize Faker

fake = Faker()

#generate fake data

def seed_data():
    for _ in range(10):
        User =User(name=fake.name(), email=fake.email())
        session.add(User)
        session.commit()
        
        for _ in range(3):
            post = post(title=fake.sesentence(), content=fake.text(), user_id=user.id)
            session.add(post)
        session.commit() 
            
if __name__ == "__main__":
    seed_data()
    print('Database seeded!')        