from sqlalchemy.orm import Session
from models.cliente import Cliente
from schemas.Cliente import ClienteBase

def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cliente).offset(skip).limit(limit).all()
    

def get_cliente(db: Session, cliente_id: str):
    return db.query(Cliente).filter(Cliente.IdCliente == cliente_id).first()

def create_cliente(db: Session, cliente: ClienteBase):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente) 
    db.commit()
    db.refresh(db_cliente)
    
    return db_cliente

def get_cliente_by_id(db: Session, id: str):
    return db.query(Cliente).filter(Cliente.IdCliente == id).first()

def delete_cliente(cliente: Cliente, db: Session):
    db.delete(cliente)
    db.commit()

    return cliente