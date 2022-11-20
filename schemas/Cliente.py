from pydantic import BaseModel


class ClienteBase(BaseModel):
    NombreEmpresa: str | None = None
    NombreContacto : str | None = None
    CargoContacto : str | None = None
    Direccion : str | None = None
    Ciudad : str | None = None
    Region : str | None = None
    CodPostal : str | None = None
    Pais : str | None = None
    Telefono : str | None = None
    Fax : str | None = None



class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    IdCliente: str 
    
    class Config:
        orm_mode = True