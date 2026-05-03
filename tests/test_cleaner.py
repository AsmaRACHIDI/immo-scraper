import pytest
from src.pipeline.cleaner import AnnonceSchema

# Données valides réutilisées dans tous les tests
VALID_DATA = {
    "titre": "Bel appartement 3 pièces",
    "url": "https://seloger.com/annonce/123",
    "source": "seloger",
    "prix": 250000.0,
    "surface": 65.0,
    "dpe": "C",
}


# Cas 1 — tout est valide
def test_annonce_with_valid_data_passes():
    annonce = AnnonceSchema(**VALID_DATA)
    assert annonce.titre == "Bel appartement 3 pièces"
    assert annonce.source == "seloger"


# Cas 2 — titre absent
def test_annonce_without_title():
    data = VALID_DATA.copy()
    data.pop("titre")
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 3 — titre vide
def test_annonce_with_empty_title():
    data = VALID_DATA.copy()
    data["titre"] = ""
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 4 — url absente
def test_annonce_without_url():
    data = VALID_DATA.copy()
    data.pop("url")
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 5 — url invalide
def test_annonce_with_invalid_url():
    data = VALID_DATA.copy()
    data["url"] = "ceci_nestpas-une-url"
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 6 — source absente
def test_annonce_without_source():
    data = VALID_DATA.copy()
    data.pop("source")
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 7 — prix négatif
def test_annonce_with_negative_price():
    data = VALID_DATA.copy()
    data["prix"] = -500.0
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 8 — surface négative
def test_annonce_with_negative_surface():
    data = VALID_DATA.copy()
    data["surface"] = -10.0
    with pytest.raises(Exception):
        AnnonceSchema(**data)


# Cas 9 — DPE invalide
def test_annonce_with_invalid_dpe():
    data = VALID_DATA.copy()
    data["dpe"] = "Z"
    with pytest.raises(Exception):
        AnnonceSchema(**data)