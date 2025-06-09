import wikipedia as wp
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class BaseResponse(BaseModel):
    title: str
    summary: str

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    title: str


@app.get("/article/{title}", response_model=BaseResponse)
def get_article(title: str):
    try:
        page = wp.page(title)
        return {
            "title": page.title,
            "summary": page.summary
        }
    except wp.exceptions.PageError:
        return {"title": "error", "summary": "Page not found"}

@app.get("/search", response_model=list[SearchResponse])
def search_articles(query: str, limit: int = 5):
    results = wp.search(query, results=limit)
    return [{"title": title} for title in results]

@app.post("/random", response_model=BaseResponse)
def get_random_article(request: SearchRequest):
    try:
        random_title = wp.random(pages=1)[0]
        page = wp.page(random_title)
        return {
            "title": page.title,
            "summary": page.summary
        }
    except wp.exceptions.PageError:
        return {"title": "error", "summary": "Page not found"}
