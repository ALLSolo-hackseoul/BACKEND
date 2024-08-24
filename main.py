import dotenv
import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from .routers import member

dotenv.load_dotenv(verbose=True)

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    member.router,
    prefix="/member",
    tags=["member"],
    responses={418: {"message": "I'm a teapot"}}
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
