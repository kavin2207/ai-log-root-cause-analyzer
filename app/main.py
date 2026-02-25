from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from app.schemas import LogRequest, IncidentResponse
from app.llm_service import analyze_logs_with_llm

app = FastAPI(title="AI Log Root Cause Analyzer")

# Enable CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.post("/analyze", response_model=IncidentResponse)
def analyze(request: LogRequest):
    return analyze_logs_with_llm(request.logs)


@app.get("/")
def serve_ui():
    return FileResponse(os.path.join(BASE_DIR, "../index.html"))
