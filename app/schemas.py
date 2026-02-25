from pydantic import BaseModel


class LogRequest(BaseModel):
    logs: str


class IncidentResponse(BaseModel):
    incident_type: str
    severity: str
    affected_service: str
    root_cause: str
    suggested_fix: str
    confidence: float
