from fastapi import FastAPI

app = FastAPI(title="Market Dashboard MVP")

@app.get("/health")
def health():
    return {"status": "ok"}
