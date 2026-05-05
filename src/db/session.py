import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Charger les variables du fichier .env
load_dotenv()


def get_database_url() -> str:
    """Construit l'URL de connexion depuis les variables d'environnement."""
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    # Vérifier que toutes les variables sont présentes
    missing = [
        var for var, val in {
            "DB_HOST": host,
            "DB_PORT": port,
            "DB_NAME": name,
            "DB_USER": user,
            "DB_PASSWORD": password,
        }.items() if not val
    ]

    if missing:
        raise ValueError(f"Variables d'environnement manquantes : {missing}")

    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


def get_engine():
    """Crée et retourne l'engine SQLAlchemy."""
    url = get_database_url()
    return create_engine(url)


def get_session():
    """Crée et retourne une session SQLAlchemy."""
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()