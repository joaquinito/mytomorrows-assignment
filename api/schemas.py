from pydantic import BaseModel, UUID4
from datetime import datetime


# Common attributes while creating or reading EAPDossier
class EAPDossier(BaseModel):
    eap_number: str
    patient: UUID4
    product: UUID4
    eap_enrollment_date: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "eap_number": "100",
                    "patient": "395bbd7b-5b54-4017-b5fe-b48cce9b1743",
                    "product": "a0c152b1-3620-45ef-a000-5d12d4076758",
                    "eap_enrollment_date": "2024-02-07T21:19:00.065Z",
                }
            ]
        }
    }


# Attributes exclusive to reading a EAPDossier
class EAPDossierWithId(EAPDossier):

    eap_dossier_id: UUID4

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "eap_number": "100",
                    "patient": "52df8b8a-019e-40ad-bb9e-1e0d408e4121",
                    "product": "52df8b8a-019e-40ad-bb9e-1e0d408e2123",
                    "eap_enrollment_date": "2024-02-07T21:19:00.065Z",
                    "eap_dossier_id": "52df8b8a-019e-40ad-bb9e-1e0d408e4dd7"
                }
            ]
        }
    }


class Patient(BaseModel):
    patient_id: UUID4
    name: str


class Product(BaseModel):
    product_id: UUID4
    name: str
