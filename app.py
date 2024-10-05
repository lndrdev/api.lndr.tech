from fastapi import FastAPI
import random

app = FastAPI(
    title="api.lndr.tech"
)

@app.get("/", description="Root endpoint")
def get_root():
    return {"message": "Welcome to my API! For more information, visit /docs."}

@app.get("/v1/joke", description="Get a random joke")
def joke(language: str = None):
    jokes = {
        "de": ["Wissenschaftler haben herausgefunden... - und sind wieder hineingenangen.",
               "Egal wie gut du fährst, Züge fahren Güter.",
               "Meine Oma arbeitet beim FBI. Wir nennen Sie jetzt Top-Siegrid.",
               "Warum können Geister so schlecht lügen? Weil man durch sie hindurchsehen kann."],

        "en": ["Why do programmers prefer dark mode? Because the light attracts bugs!",
                "Why was the math book sad? It had too many problems.",
                "Why don’t skeletons fight each other? They don’t have the guts.",
                "Why did the coffee file a police report? It got mugged."]
    }
    joke = random.choice(jokes.get(language if language else "de", jokes["de"]))
    return {"joke": joke}