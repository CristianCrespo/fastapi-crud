from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentails=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check/")
def health-check():
    return "Ok"
