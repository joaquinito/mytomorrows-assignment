from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from .database import Base


# SQLAlchemy model for table 'eap_dossier'
class EAPDossier(Base):
    __tablename__ = "eap_dossier"

    # uuid.uuid4 generates a random UUID
    eap_dossier_id = Column(UUID(as_uuid=True), primary_key=True,
                            default=uuid.uuid4)
    eap_number = Column(String)
    patient = Column(UUID(as_uuid=True),
                     ForeignKey("patient.patient_id"))
    product = Column(UUID(as_uuid=True),
                     ForeignKey("product.product_id"))
    eap_enrollment_date = Column(DateTime)

    patient_model = relationship("Patient", foreign_keys=[patient])
    product_model = relationship("Product", foreign_keys=[product])


# SQLAlchemy model for table 'patient'
class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(UUID(as_uuid=True), primary_key=True,
                        default=uuid.uuid4)
    name = Column(String)


# SQLAlchemy model for table 'product'
class Product(Base):
    __tablename__ = "product"

    product_id = Column(UUID(as_uuid=True), primary_key=True,
                        default=uuid.uuid4)
    name = Column(String)
