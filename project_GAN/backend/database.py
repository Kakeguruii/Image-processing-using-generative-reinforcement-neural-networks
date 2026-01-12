from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import Config
import boto3

s3 = boto3.client('s3')
s3.upload_file(file_path, 'bucket-name', 'image-key')

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()
