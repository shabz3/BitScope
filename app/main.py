from fastapi import FastAPI, HTTPException, Request, Response
import os
import requests
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from loguru import logger
from prometheus_fastapi_instrumentator import Instrumentator

# Debug
# import uvicorn

app = FastAPI()

BASE_URL = os.environ.get("BASE_URL", "https://api.coingecko.com")
logger.info(f"BASE_URL: {BASE_URL}")


# Needed for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_coingecko_stats(request: Request):
    url = f"{BASE_URL}/api/v3/exchange_rates"
    logger.info(f"URL is: {url}")
    try:
        return_json = requests.get(url).json()
        all_items = list(return_json["rates"].items())
        logger.debug(f"JSON returned with all values: {return_json}")
    except Exception as e:
        logger.error(f"Unable to fetch: {e}")
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

# Expose Prometheus metrics for FastAPI
instrumentator = Instrumentator()
Instrumentator().instrument(app).expose(app)

## Debug
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
