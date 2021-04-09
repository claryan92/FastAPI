from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_username(db: Session, username: str):
    """Get specified user info from database"""
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user in the database"""
    hashed_password = f"{user.password} not actually hashed"
    db_user = models.UserInfo(username=user.username, password=hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.refresh(db_user)
    return db_user