from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from deps import get_db 
from shortener import create_short_url
from DataBase.crud import create_url, get_url, delete_url, get_stats
from caching.redis import redis_client


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def normalize(code: str):
    return code.replace("http://", "").replace("https://", "").split("/")[-1]

class URLRequest(BaseModel):
    long_url: str

@app.post("/shorten")
def shorten_url(data: URLRequest, db: Session = Depends(get_db)):
    short_code = create_short_url(data.long_url)

    create_url(db, short_code, data.long_url)

    redis_client.set(short_code, data.long_url)
    redis_client.set(f"stats:{short_code}", -1)

    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }


@app.delete("/delete/{short_code}")
def delete_short(short_code: str, db: Session = Depends(get_db)):
    short_code = normalize(short_code)

    url = delete_url(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    redis_client.delete(short_code)
    redis_client.delete(f"stats:{short_code}")

    return {"message": "Deleted"}


@app.get("/stats/{short_code}")
def stats(short_code: str, db: Session = Depends(get_db)):
    short_code = normalize(short_code)

    clicks = redis_client.get(f"stats:{short_code}")
    if clicks!=-1:
        return {"short_code": short_code,  "clicks": int(clicks)}

    url = get_stats(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    redis_client.set(f"stats:{short_code}", url.clicks)

    return {"clicks": url.clicks}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    short_code = normalize(short_code)

    url = redis_client.get(short_code)
    if url:
        redis_client.incr(f"stats:{short_code}")
        return RedirectResponse(url)

    url = get_url(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    redis_client.set(short_code, url.long_url)

    url.clicks += 1
    db.commit()

    return RedirectResponse(url.long_url)
