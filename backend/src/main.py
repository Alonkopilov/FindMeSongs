import math
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.training import get_similar_songs
from src.training import DATASET_DF

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"]
)


@app.get("/")
async def root():
    return {"message": "Hello Kubernetes"}


@app.get("/find_songs/")
async def fetch_similar_songs(name: str, artist: str, amount: int):
    if name == "" or artist == "" or amount < 0:
        raise HTTPException(status_code=400, detail="Please enter non-empty values.")

    similar_songs_df = get_similar_songs(name, artist, amount)

    if similar_songs_df is None:
        raise HTTPException(status_code=400, detail="Song/Artist was not found.")

    return similar_songs_df.to_dict(orient='records')


@app.get("/search/")
async def search_songs(query: str):
    results = DATASET_DF[
        DATASET_DF['artist+song'].str.contains(query, case=False)
    ]['artist+song'].head(10).tolist()

    return {"result": results}
