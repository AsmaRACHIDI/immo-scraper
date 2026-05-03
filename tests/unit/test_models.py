from src.db.models import Annonce

def test_annonce_with_valid_fields_is_created():
    annonce = Annonce(
        titre="Bel appartement 3 pièces",
        type_bien="appartement",
        transaction="achat",
        prix=250000.0,
        surface=65.0,
        ville="Paris",
        code_postal="75011",
        url="https://seloger.com/annonce/123",
        source="seloger",
    )
    assert annonce.titre == "Bel appartement 3 pièces"
    assert annonce.prix == 250000.0
    assert annonce.ville == "Paris"