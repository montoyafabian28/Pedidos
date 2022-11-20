from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from config.db import Base

class Cliente(Base):
    __tablename__ = 'Cliente'
    IdCliente = Column(String(10), primary_key=True)
    NombreEmpresa = Column(String(80))
    NombreContacto = Column(String(60))
    CargoContacto = Column(String(60))
    Direccion = Column(String(120))
    Ciudad = Column(String(30))
    Region = Column(String(30))
    CodPostal = Column(String(20))
    Pais = Column(String(30))
    Telefono = Column(String(48))
    Fax = Column(String(48))
