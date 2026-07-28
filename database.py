from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# MySQL Database Connection
DATABASE_URL = "mysql+pymysql://root:2004@localhost:3306/ecommerce_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
