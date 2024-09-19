from models import User, Post, Base
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Setup database
engine = create_engine('sqlite:///your_database_name.db')  # Make sure the path is correct
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
fake = Faker()

# Generate fake data
def seed_data():
    for _ in range(10):
        user = User(name=fake.name(), email=fake.email())  # Create a new User instance
        session.add(user)
        session.commit()  # Commit after adding the user to get the user.id
        
        for _ in range(3):
            post = Post(title=fake.sentence(), content=fake.text(), user_id=user.id)  # Create a new Post instance
            session.add(post)  # Add each post to the session
        session.commit()  # Commit after adding all posts for the user

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Ensure tables are created before seeding
    seed_data()  # Seed the data
    print('Database seeded!')
