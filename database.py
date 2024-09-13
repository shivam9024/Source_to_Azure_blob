from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta

# Define the PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:Shivam123@localhost:5432/Amplifisource"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Test connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print(f"An error occurred: {e}")


# Define the base class for models
Base: DeclarativeMeta = declarative_base()

# Define the SessionLocal class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session for API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()