import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session

DB_USER =  "root" #os.getenv("DB_USER") #"root"
DB_PASSWORD = "RootPassword" #os.getenv("DB_PASSWORD") #"RootPassword"
DB_HOST = "localhost" # os.getenv("DB_HOST") "kanastra-database"
DB_NAME = "Kanastra" #os.getenv("DB_NAME")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
