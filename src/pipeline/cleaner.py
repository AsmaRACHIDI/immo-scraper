from pydantic import BaseModel, field_validator, HttpUrl
from typing import Optional

class AnnonceSchema(BaseModel):
    # Champs obligatoires
    titre: str
    url: HttpUrl
    source: str

    # Champs optionnels
    description: Optional[str] = None
    type_bien: Optional[str] = None
    transaction: Optional[str] = None
    prix: Optional[float] = None
    charges: Optional[float] = None
    surface: Optional[float] = None
    nb_pieces: Optional[int] = None
    etage: Optional[int] = None
    adresse: Optional[str] = None
    ville: Optional[str] = None
    code_postal: Optional[str] = None
    departement: Optional[str] = None
    contact_nom: Optional[str] = None
    contact_tel: Optional[str] = None
    dpe: Optional[str] = None

    @field_validator("titre")
    @classmethod
    def titre_ne_doit_pas_etre_vide(cls, valeur):
        if not valeur.strip():
            raise ValueError("le titre ne peut pas être vide")
        return valeur

    @field_validator("prix")
    @classmethod
    def prix_doit_etre_positif(cls, valeur):
        if valeur is not None and valeur < 0:
            raise ValueError("le prix doit être positif")
        return valeur

    @field_validator("surface")
    @classmethod
    def surface_doit_etre_positive(cls, valeur):
        if valeur is not None and valeur < 0:
            raise ValueError("la surface doit être positive")
        return valeur

    @field_validator("dpe")
    @classmethod
    def dpe_doit_etre_valide(cls, valeur):
        valeurs_valides = ["A", "B", "C", "D", "E", "F", "G"]
        if valeur is not None and valeur not in valeurs_valides:
            raise ValueError(f"le DPE doit être parmi {valeurs_valides}")
        return valeur