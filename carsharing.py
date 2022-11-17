from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    """Return a message"""
    return {'message': "Welcome to the Car Sharing Hub!"}
