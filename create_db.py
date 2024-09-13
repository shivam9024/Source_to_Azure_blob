import models
from database import engine

# Create all tables
models.Base.metadata.create_all(bind=engine)