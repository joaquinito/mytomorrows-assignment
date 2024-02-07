from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from .database import Base


class EAP_Dossier(Base):
    __tablename__ = "eap_dossier"
    
    eap_dossier_id = Column(UUID(as_uuid=True), primary_key=True,
                            default=uuid.uuid4)  # uuid.uuid4 generates a random UUID
    eap_number = Column(String)
    patient = Column(String)
    product = Column(String)
    eap_enrollment_date = Column(DateTime)
