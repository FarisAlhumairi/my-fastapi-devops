from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome Faris! My DevOps Journey Starts Here 🚀"}
