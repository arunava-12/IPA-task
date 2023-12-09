from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn

app = FastAPI()

origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wiki/{query}")
def search_wikipedia(query: str):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'exintro': True,  
        'explaintext': True,  
        'utf8': 1,
        'titles': query
    }

    data = requests.get(url, params=params).json()

    pages = data.get('query', {}).get('pages', {})
    if not pages:
        raise HTTPException(status_code=404, detail="Page not found")

    page_id, page_info = pages.popitem()

    title = page_info.get('title', '')
    summary = page_info.get('extract', '')

    return {"title": title, "summary": summary}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
