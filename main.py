from fastapi import FastAPI
from database import engine, Base

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Ride-hailing API is live!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

