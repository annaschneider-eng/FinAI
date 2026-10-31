
from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models.transaction import Transaction

# Criar as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinAI API",
    description="Assistente Financeiro Inteligente",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Bem-vindo ao FinAI!",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "FinAI"
    }


@app.get("/about")
def about():
    return {
        "project": "FinAI",
        "description": "Assistente financeiro com inteligência artificial",
        "technologies": [
            "Python",
            "FastAPI",
            "SQL",
            "Machine Learning",
            "LLM"
        ]
    }
