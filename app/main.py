from fastapi import FastAPI, HTTPException, Request
import os
import requests

# import uvicorn
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

BASE_URL = os.environ.get("BASE_URL", "https://api.coingecko.com")

# Needed for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_coingecko_stats(request: Request):
    url = f"{BASE_URL}/api/v3/exchange_rates"
    try:
        return_json = requests.get(url).json()
        all_items = list(return_json["rates"].items())
    except:
        raise HTTPException(status_code=500, detail="Failed to fetch")
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "items": all_items,
        },
    )


# Redirects everything else to 404 page
@app.exception_handler(404)
async def custom_404_handler(request, __):
    return templates.TemplateResponse(
        request=request, name="404.html", context={"request": request}
    )


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
