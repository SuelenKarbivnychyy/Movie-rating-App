"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db



def create_user(email, password):
    """Create and return a new user."""

    user = User(email='dimma@gmail.com', password='123')

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)