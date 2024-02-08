from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .models import EAPDossier as model_EAP_Dossier
from .schemas import EAPDossierWithId as schema_EAP_DossierW


def db_get_eap_dossiers(db: Session, limit: int = 100):
    return db.query(model_EAP_Dossier).limit(limit).all()


def db_get_eap_dossier_by_id(db: Session, eap_dossier_id: str):
    return db.query(model_EAP_Dossier).filter(
        model_EAP_Dossier.eap_dossier_id == eap_dossier_id).first()


def db_create_eap_dossier(db: Session, eap_dossier: schema_EAP_DossierW):

    new_eap_dossier = model_EAP_Dossier(
        eap_number=eap_dossier.eap_number,
        patient=eap_dossier.patient,
        product=eap_dossier.product,
        eap_enrollment_date=eap_dossier.eap_enrollment_date
    )

    try:
        db.add(new_eap_dossier)
        db.commit()
        # This will add the generated UUID to this object
        db.refresh(new_eap_dossier)
    except (IntegrityError):
        raise HTTPException(status_code=400, detail="Product or Patient ID are invalid")

    return new_eap_dossier


def db_update_eap_dossier(db: Session, eap_dossier_id: str,
                          eap_dossier: schema_EAP_DossierW):

    target = db.query(model_EAP_Dossier).filter(
        model_EAP_Dossier.eap_dossier_id == eap_dossier_id).first()
    if target is None:
        raise HTTPException(status_code=404, detail="EAP Dossier not found")

    target.eap_number = eap_dossier.eap_number
    target.patient = eap_dossier.patient,
    target.product = eap_dossier.product,
    target.eap_enrollment_date = eap_dossier.eap_enrollment_date

    db.commit()
    db.refresh(target)

    return target


def db_delete_eap_dossier(db: Session, eap_dossier_id: str):

    db.query(model_EAP_Dossier).filter_by(
        eap_dossier_id=eap_dossier_id).delete()
    db.commit()

    return {"message": "EAP Dossier successfully deleted."}
