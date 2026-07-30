from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# MySQL Database Connection
DATABASE_URL = "mysql://avnadmin:AVNS_KaQ-79hOzWJIXvNWcRw@mysql-12f443d8-saisree-3c10.j.aivencloud.com:28388/default"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
