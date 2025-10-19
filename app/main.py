from fastapi import FastAPI, Request
import os
import requests
import uvicorn
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_URL = os.environ.get("BASE_URL", "https://api.coingecko.com")

# Needed for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_coingecko_stats(request: Request):
    url = f"{BASE_URL}/api/v3/exchange_rates"
    return_json = requests.get(url).json()
    all_items = list(return_json["rates"].items())
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "items": all_items,
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
