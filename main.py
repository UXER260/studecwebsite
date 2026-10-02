from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles

# Initialize the FastAPI app
app = FastAPI(title="Event Landing Page")

# Mount the static directory to serve CSS and images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the template engine
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def serve_homepage(request: Request):
    # Render the index.html template when visiting the root URL
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    # Run the server on http://127.0.0.1:8000
    uvicorn.run("main:app", host="0.0.0.0", port=6522, reload=True)
