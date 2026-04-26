from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows access from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows any method
    allow_headers=["*"]  # Allows any headers
)

@app.get("/process-task")
async def process_task(task_id: int):
    """Process a given task"""
    return {"task_id": task_id, "status": "processed"}

@app.get("/text-analysis")
async def text_analysis(text: str):
    """Analyze the given text"""
    return {"text": text, "analysis": "analysis results"}

@app.get("/data-analysis")
async def data_analysis(data_id: int):
    """Analyze the given data"""
    return {"data_id": data_id, "results": "analysis results"}

@app.get("/model-management/{model_id}")
async def model_management(model_id: str):
    """Manage a specified model"""
    return {"model_id": model_id, "status": "model managed"}