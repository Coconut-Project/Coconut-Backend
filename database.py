from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import *
from app.models import *
from base import Base
from dotenv import load_dotenv
import os

load_dotenv()

# db_username = os.getenv("DB_USERNAME")
# db_password = os.getenv("DB_PASSWORD")
# db_host = os.getenv("DB_HOST")
# db_name = os.getenv("DB_NAME")

# URL_DATABASE = f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}"

EXTERNAL_DATABASE_URL = os.getenv("EXTERNAL_DATABASE_URL")

if not EXTERNAL_DATABASE_URL:
    raise ValueError(
        "EXTERNAL_DATABASE_URL n'est pas défini dans les variables d'environnement"
    )

engine = create_engine(EXTERNAL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in my pg db
Base.metadata.create_all(bind=engine)


# for each request, we generate a session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
