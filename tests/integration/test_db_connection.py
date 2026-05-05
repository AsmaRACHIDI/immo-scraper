import pytest
from sqlalchemy import text
from src.db.session import get_engine, get_session
from src.db.models import Base


def test_engine_connects_to_database():
    """Vérifie qu'on peut se connecter à PostgreSQL"""
    engine = get_engine()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_tables_are_created():
    """Vérifie que les tables sont bien créées en base"""
    engine = get_engine()
    Base.metadata.create_all(engine)
    assert "annonces" in engine.dialect.get_table_names(engine.connect())


def test_session_can_insert_and_read_annonce():
    """Vérifie qu'on peut insérer et relire une annonce"""
    from src.db.models import Annonce

    session = get_session()

    # Insérer une annonce de test
    annonce = Annonce(
        titre="Test appartement",
        url="https://seloger.com/test/123",
        source="seloger",
    )
    session.add(annonce)
    session.commit()

    # Relire depuis la base
    result = session.query(Annonce).filter_by(titre="Test appartement").first()
    assert result is not None
    assert result.source == "seloger"

    # Nettoyer — supprimer la donnée de test
    session.delete(result)
    session.commit()
    session.close()