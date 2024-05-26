import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager


def init_app():
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        print("Server started")
        # await connect
        yield
        print("Shutdown server")
        # await disconnect
    app = FastAPI(
        title="Nigell Marcel Jama Oyarvide",
        description="FastAPI Prisma",
        version="1.0.0",
        lifespan=lifespan
    )

    @app.get("/")
    def home():
        return "Welcome Home!"

    return app


app = init_app()

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8888, reload=True)
