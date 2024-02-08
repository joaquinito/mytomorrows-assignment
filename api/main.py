from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from mangum import Mangum

from .crud import (db_get_eap_dossiers, db_get_eap_dossier_by_id,
                   db_create_eap_dossier, db_delete_eap_dossier,
                   db_update_eap_dossier)
from .schemas import (EAPDossier as schema_EAP_DossierBase,
                      EAPDossierWithId as schema_EAPDossierWithId)
from .database import SessionLocal

app = FastAPI()


# Get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_landing_message() -> str:
    return "Ricardo's solution for MyTomorrows' assignment."


@app.get("/api/eap_dossiers")
def read_eap_dossiers(limit: int = 100, db: Session = Depends(get_db)) \
        -> list[schema_EAPDossierWithId]:
    eap_dossiers = db_get_eap_dossiers(db, limit=limit)
    return eap_dossiers


@app.get("/api/eap_dossiers/{id}")
def read_eap_dossier(id: str, db: Session = Depends(get_db)):

    eap_dossier = db_get_eap_dossier_by_id(db=db, eap_dossier_id=id)

    patient_info = {
        "patient_id": str(eap_dossier.patient_model.patient_id),
        "name": eap_dossier.patient_model.name}
    product_info = {
        "product_id": str(eap_dossier.product_model.product_id),
        "name": eap_dossier.product_model.name}

    extended_eap_dossier_data = {
        "eap_number": eap_dossier.eap_number,
        "patient": patient_info,
        "product": product_info,
        "eap_enrollment_date": eap_dossier.eap_enrollment_date.isoformat(),
        "eap_dossier_id": str(eap_dossier.eap_dossier_id)
    }

    return extended_eap_dossier_data


@app.post("/api/eap_dossiers")
def create_eap_dossier(eap_dossier: schema_EAP_DossierBase,
                       db: Session = Depends(get_db)):
    return db_create_eap_dossier(db=db, eap_dossier=eap_dossier)


@app.put("/api/eap_dossiers/{id}")
def update_eap_dossier(id: str, eap_dossier: schema_EAPDossierWithId,
                       db: Session = Depends(get_db)):
    return db_update_eap_dossier(db=db, eap_dossier_id=id,
                                 eap_dossier=eap_dossier)


@app.delete("/api/eap_dossiers/{id}")
def delete_eap_dossier(id: str, db: Session = Depends(get_db)):
    return db_delete_eap_dossier(db=db, eap_dossier_id=id)


# Mangum provides an adapter to run ASGI applications in AWS Lambda
handler = Mangum(app)
1
