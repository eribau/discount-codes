from fastapi import FastAPI

from routers import discount_codes

app = FastAPI()

app.include_router(discount_codes.router)