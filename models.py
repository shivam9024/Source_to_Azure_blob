# models.py
from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

class AzureStorage(Base):
    __tablename__ = 'azure_storage'
    
    source_id = Column(Integer, ForeignKey('sources.id'), primary_key=True)
    container_name = Column(String(255), nullable=False)
    sas_url = Column(String(255), nullable=False)
    
    # Relationship to Source
    source = relationship("Source", back_populates="azure_storage")

class Organization(Base):
    __tablename__ = 'organizations'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), nullable=False, index=True)
    domain = Column(String(100), nullable=True)  # New field
    description = Column(Text, nullable=True)    # New field
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())  # New field
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())  # New field
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)  # New field

    # Relationship to Workspace
    workspaces = relationship("Workspace", back_populates="organization")

class Workspace(Base):
    __tablename__ = 'workspaces'
    
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    name = Column(String(40), index=True, unique=False, nullable=False)
    is_active = Column(Boolean, default=True)
    description = Column(Text, nullable=True)
    processed_chunks = Column(Integer, default=0)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    
    # Relationship to Organization
    organization = relationship("Organization", back_populates="workspaces")

    # Relationship to File
    files = relationship("File", back_populates="workspace")


class File(Base):
    __tablename__ = 'files'
    
    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey('workspaces.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    mimetype = Column(String(100), nullable=False)
    size = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    
    # Relationship to Workspace
    workspace = relationship("Workspace", back_populates="files")

# Add a relationship to Workspace
Workspace.files = relationship("File", back_populates="workspace")


class Source(Base):
    __tablename__ = 'sources'
    
    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey('workspaces.id'), nullable=False)
    source_type = Column(String(50), nullable=False)
    # container_name = Column(String(255), nullable=False)
    # sas_url = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    
    # Relationship to Workspace
    workspace = relationship("Workspace", back_populates="sources")

     
    # Relationship to AzureStorage
    azure_storage = relationship("AzureStorage", uselist=False, back_populates="source")

# Update the Workspace model to include the relationship
Workspace.sources = relationship("Source", back_populates="workspace")
