from pydantic import BaseModel, UUID4
from datetime import datetime


# Common attributes while creating or reading EAP_Dossier
class EAP_DossierBase(BaseModel):
    eap_number: str
    patient: str
    product: str
    eap_enrollment_date: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                  "eap_number": "100",
                  "patient": "John Doe",
                  "product": "Product X",
                  "eap_enrollment_date": "2024-02-07T21:19:00.065Z",
                }
            ]
        }
    }


# Attributes exclusive to reading a EAP_Dossier
class EAP_Dossier(EAP_DossierBase):
    
    eap_dossier_id: UUID4

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                  "eap_number": "100",
                  "patient": "John Doe",
                  "product": "Product X",
                  "eap_enrollment_date": "2024-02-07T21:19:00.065Z",
                  "eap_dossier_id": "52df8b8a-019e-40ad-bb9e-1e0d408e4dd7"
                }
            ]
        }
    }
