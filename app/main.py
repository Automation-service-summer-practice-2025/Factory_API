from fastapi import FastAPI
from app.stations.router import router as router_stations
from app.elements.router import router as router_elements
from app.documents.router import router as router_documents


app = FastAPI()


@app.get("/")
async def home():
   return {"data": "Hello World"}


app.include_router(router_stations)
app.include_router(router_elements)
app.include_router(router_documents)