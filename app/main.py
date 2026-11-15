
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.nasa import router as nasa_router
from app.api.soil import router as soil_router
from app.api.rotation import router as rotation_router
from app.api.farmers_fields import router as farmers_fields_router

app = FastAPI(
    title="AgroVision AI",
    description="AI-powered Smart Agriculture Platform",
    version="1.3.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://agrovision-demo-six.vercel.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5175"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nasa_router)
app.include_router(soil_router)
app.include_router(rotation_router)
app.include_router(farmers_fields_router)


@app.get("/")
def home():
    return {
        "project": "AgroVision AI",
        "status": "running",
        "message": "Agriculture AI Platform is online"
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "message": "AgroVision AI backend is working"
    }


@app.get("/api/crops")
def get_crops():
    return {
        "crops": [
            "Wheat",
            "Mung bean",
            "Cotton",
            "Alfalfa",
            "Maize",
            "Sorghum",
            "Chickpea",
            "Pea",
            "Sunflower"
        ]
    }
