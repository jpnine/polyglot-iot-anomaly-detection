from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class SensorInput(BaseModel):
    machineId: str
    temperature: float
    time: datetime

@app.post("/analyze")
async def analyze_sensor_data(data: SensorInput) -> dict:
    # Logic: Detect if temperature exceeds threshold
    if data.temperature > 100:
        return {"anomaly": True}
    else:
        return {"anomaly": False}