from datetime import datetime

from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Annonce(Base):
    __tablename__ = "annonces"

    # Identifiant unique — auto-incrémenté par PostgreSQL
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Infos principales
    titre = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    type_bien = Column(String(100), nullable=True)
    transaction = Column(String(50), nullable=True)

    # Prix
    prix = Column(Numeric(12, 2), nullable=True)
    charges = Column(Numeric(8, 2), nullable=True)

    # Caractéristiques
    surface = Column(Numeric(8, 2), nullable=True)
    nb_pieces = Column(Integer, nullable=True)
    etage = Column(Integer, nullable=True)
    dpe = Column(String(1), nullable=True)

    # Localisation
    adresse = Column(String(500), nullable=True)
    ville = Column(String(200), nullable=True)
    code_postal = Column(String(10), nullable=True)
    departement = Column(String(200), nullable=True)

    # Contact
    contact_nom = Column(String(200), nullable=True)
    contact_tel = Column(String(50), nullable=True)

    # Métadonnées
    url = Column(Text, nullable=False)
    source = Column(String(50), nullable=False)
    date_scraping = Column(DateTime, default=datetime.now)