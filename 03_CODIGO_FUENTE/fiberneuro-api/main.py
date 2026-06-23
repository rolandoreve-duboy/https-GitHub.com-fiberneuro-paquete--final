"""
API Principal - FiberNeuro Backend
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Crear aplicación
app = FastAPI(
    title="FiberNeuro API",
    description="API Backend para el sistema de gestión FiberNeuro",
    version="1.0.0"
)

# Configurar CORS
origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Ruta raíz de verificación"""
    return {
        "message": "API FiberNeuro",
        "status": "active",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    """Verificar estado de la API"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
