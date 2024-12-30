from fastapi import FastAPI
from app.api.endpoints import odoo_inbound
from app.core.logging_config import logger

app = FastAPI()

# Include the Odoo router
app.include_router(odoo_inbound.router, prefix="/api", tags=["odoo"])

# Example of using the logger
@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI application startup")
