from fastapi import FastAPI, Response, status
from mangum import Mangum

app = FastAPI()

app.mount("/", StaticFiles(directory="app", html=True), name="app")


@app.get("/500")
async def internal_server_error(response: Response):
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

@app.get("/400")
async def not_found(response: Response):
    response.status_code = status.HTTP_400_BAD_REQUEST

@app.get("/items/{item_id}")
async def read_item(item_id, response: Response):
    response.status_code = status.HTTP_200_OK
    return { "item_id": item_id}

handler = Mangum(app, lifespan="off")
