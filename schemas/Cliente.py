from pydantic import BaseModel
from datetime import date

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

class PedidoBase(BaseModel):
    IdPedido : int | None = None 
    IdCliente : str | None = None
    IdEmpleado : int | None = None
    FechaPedido : str | None = None
    FechaEntrega : str | None = None
    FechaEnvio : str | None = None
    IdEmpresasTransporte : int | None = None
    Cargo : float | None = None
    Destinatario : str | None = None
    DireccionDestinatario : str | None = None
    CiudadDestinatario : str | None = None
    RegionDestinatario : str | None = None
    CodPostalDestinatario : str | None = None
    PaisDestinatario : str | None = None

    class config:
        orm_mode = True