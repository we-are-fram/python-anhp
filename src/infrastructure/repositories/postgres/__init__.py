from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from config.config import settings

engine = create_engine(settings.DB_URI)
BaseModel = declarative_base()
# BaseModel.metadata.bind = engine
