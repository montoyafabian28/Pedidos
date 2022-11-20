from sqlalchemy.orm import Session
from models.cliente import Cliente

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cliente).offset(skip).limit(limit).all()
    

def get_user(db: Session, user_id: str):
    return db.query(Cliente).filter(Cliente.IdCliente == user_id).first()