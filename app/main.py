from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # <-- Define app first

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sonar-frontend-smoky.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}