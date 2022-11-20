from pydantic import BaseModel


class ClienteBase(BaseModel):
    IdCliente: str
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

    class Config:
        orm_mode = True

