from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import metadata, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=metadata)

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    projects = relationship("Project", back_populates="client")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    budget = Column(Float)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", back_populates="projects")
    payments = relationship("Payment", back_populates="project")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    date = Column(Date)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="payments")

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

