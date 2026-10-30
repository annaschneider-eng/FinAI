
from fastapi import FastAPI

# Criando a aplicação
app = FastAPI(
    title="FinAI API",
    description="Assistente Financeiro Inteligente",
    version="1.0.0"
)


# Rota inicial
@app.get("/")
def home():
    return {
        "message": "Bem-vindo ao FinAI!",
        "status": "online"
    }


# Rota de verificação
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "FinAI"
    }


# Rota de apresentação do sistema
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
