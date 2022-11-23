from fastapi import APIRouter, Depends, HTTPException
from config.db import engine, SessionLocal
import models.cliente
import schemas.crud_cliente as crud
import schemas.crud_pedidos as crud_pedidos
from sqlalchemy.orm import Session
from schemas.Cliente import ClienteBase, PedidoBase

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
    clientes = crud.get_clientes(db, skip=skip, limit=limit)
    return clientes

@cliente.get('/pedidos')
async def getPedidos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pedidos = crud_pedidos.get_pedidos(db,skip,limit)
    return pedidos

@cliente.get('/pedido/{id}')
async def getPedido(id: int, db: Session = Depends(get_db)):
    db_pedido = crud_pedidos.get_pedido(db, id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail='Pedido not found')
    return db_pedido

@cliente.get('/producto/{id}')
async def getProducto(id: int, db: Session = Depends(get_db)):
    db_producto = crud_pedidos.get_producto(db, id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail='producto not found')
    return db_producto

@cliente.get('/detallesPedidos/{id}')
async def getDetallesPedidos(id: int, db: Session = Depends(get_db)):
    db_dPedido = crud_pedidos.get_detallesPedidos(db, id)
    if db_dPedido is None:
        raise HTTPException(status_code=404, detail='detalles not found')
    return db_dPedido



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

@cliente.put('/clientes')
async def updateCliente(cliente: ClienteBase, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente_by_id(db,cliente.IdCliente)
    if db_cliente is not None:
        return crud.update_cliente(db_cliente,db)
    else:
        raise HTTPException(status_code=400, detail='Bad client data')