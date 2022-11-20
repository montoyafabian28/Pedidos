from fastapi import APIRouter, Depends, HTTPException
from config.db import engine, SessionLocal
import models.cliente
import schemas.crud_cliente as crud
from sqlalchemy.orm import Session
from schemas.Cliente import Cliente

models.cliente.Base.metadata.create_all(engine)

cliente = APIRouter()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@cliente.get('/clientes', response_model=list[Cliente])
async def getClientes(skip: int = 0, limit: int = 10,db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@cliente.get('/cliente/{id}', response_model=Cliente)
async def getCliente(id: str,db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id = id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user

