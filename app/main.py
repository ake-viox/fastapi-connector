from typing import Union

from fastapi import FastAPI

app = FastAPI()

# Include the Odoo router
app.include_router(odoo_inbound.router, prefix="/api", tags=["odoo"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
