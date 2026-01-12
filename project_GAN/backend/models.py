from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    upload_date = Column(Date)
    processed_image = relationship("ProcessedImage", backref="image")

class ProcessedImage(Base):
    __tablename__ = 'processed_images'
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey('images.id'))
    style = Column(String)
    processing_date = Column(Date)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
