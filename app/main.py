from fastapi import FastAPI

app = FastAPI()


@app.get("/health-check/")
def health_check():
    """
    Return just a message to check the app is working.
    """
    return {"message": "OK"}
