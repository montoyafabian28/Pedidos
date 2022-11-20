from fastapi import APIRouter, Depends, HTTPException
from config.db import engine, SessionLocal
import models.cliente
import schemas.crud_cliente as crud
from sqlalchemy.orm import Session
from schemas.Cliente import ClienteBase

models.cliente.Base.metadata.create_all(engine)

cliente = APIRouter()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@cliente.get('/clientes', response_model=list[ClienteBase])
async def getClientes(skip: int = 0, limit: int = 10,db: Session = Depends(get_db)):
    users = crud.get_clientes(db, skip=skip, limit=limit)
    return users


@cliente.get('/cliente/{id}', response_model=ClienteBase)
async def getCliente(id: str,db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db, cliente_id=id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_cliente

@cliente.post('/clientes', response_model=ClienteBase)
async def createCliente(cliente: ClienteBase, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente_by_id(db, cliente.IdCliente)
    if db_cliente:
        raise HTTPException(status_code=400, detail='Cliente ya existente')

    return crud.create_cliente(db,cliente)

@cliente.delete('/cliente/{id}', response_model=ClienteBase)
async def deleteCliente(id: str, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente_by_id(db, id)
    if db_cliente is not None:
        return crud.delete_cliente(db_cliente,db)
    else:
        raise HTTPException(status_code=400, detail='Bad Id')