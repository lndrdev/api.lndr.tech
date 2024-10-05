from fastapi import FastAPI
import random

app = FastAPI(
    title="api.lndr.tech"
)
@app.get("/", description="Root endpoint")
def get_root():
    return {"message": "Welcome to my API! For more information, visit /docs."}

@app.get("/v1/zitat")
def zitat():
    zitate = [
    "Auf drei sagen wir alle 'Hamburger Royale TS'"
]
    random_zitat = random.choice(zitate)
    return {"zitat": random_zitat}