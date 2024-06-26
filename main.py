from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sql, image, voice, html_pages  # Import the new router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with appropriate origins in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Include routers
app.include_router(sql.router)
app.include_router(image.router)
app.include_router(voice.router)
app.include_router(html_pages.router)  # Include the router for HTML pages

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
