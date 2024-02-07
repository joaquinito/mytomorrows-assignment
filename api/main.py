from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from mangum import Mangum

from .crud import (db_get_eap_dossiers, db_get_eap_dossier_by_id,
                   db_create_eap_dossier, db_delete_eap_dossier,
                   db_update_eap_dossier)
from .schemas import (EAP_DossierBase as schema_EAP_DossierBase,
                      EAP_Dossier as schema_EAP_Dossier)                   
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
def read_eap_dossiers(limit: int = 100, db: Session = Depends(get_db)) -> list[schema_EAP_Dossier]:
    eap_dossiers = db_get_eap_dossiers(db, limit=limit)
    return eap_dossiers


@app.get("/api/eap_dossiers/{id}")
def read_eap_dossier(id: str, db: Session = Depends(get_db)) -> schema_EAP_Dossier:
    eap_dossier = db_get_eap_dossier_by_id(db=db, eap_dossier_id=id)
    return eap_dossier


@app.post("/api/eap_dossiers")
def create_eap_dossier(eap_dossier: schema_EAP_DossierBase, db: Session = Depends(get_db)):
    return db_create_eap_dossier(db=db, eap_dossier=eap_dossier)


@app.put("/api/eap_dossiers/{id}")
def update_eap_dossier(id: str, eap_dossier: schema_EAP_Dossier, db: Session = Depends(get_db)):
    return db_update_eap_dossier(db=db, eap_dossier_id=id, eap_dossier=eap_dossier)


@app.delete("/api/eap_dossiers/{id}")
def delete_eap_dossier(id: str, db: Session = Depends(get_db)):
    return db_delete_eap_dossier(db=db, eap_dossier_id=id)


# Mangum provides an adapter to run ASGI applications in AWS Lambda
handler = Mangum(app)
