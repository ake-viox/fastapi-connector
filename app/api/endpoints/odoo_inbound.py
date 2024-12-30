from fastapi import APIRouter, Request, status
from pydantic import BaseModel
from typing import Optional
from app.core.logging_config import logger

router = APIRouter()

class StockPickingData(BaseModel):
    picking_id: int
    origin: Optional[str] = None
    partner_id: Optional[int] = None
    location_id: Optional[int] = None
    location_dest_id: Optional[int] = None
    # ... add the fields you want to handle from Odoo

@router.post("/odoo/stock_picking", status_code=status.HTTP_201_CREATED)
async def receive_stock_picking(data: StockPickingData):
    """
    Endpoint to receive data from Odoo stock.picking.
    
    Example request body:
    {
      "picking_id": 123,
      "origin": "SO1234",
      "partner_id": 45,
      "location_id": 10,
      "location_dest_id": 15
    }
    """
    # Here you can process, store, or forward the data
    # For now, just print or log it
    print("Received stock picking data:", data)

    # Log the received data
    logger.info(f"Received stock picking data: {data.json()}")

    # Return a response to confirm receipt
    return {
        "message": "Stock picking data received",
        "data": data
    }
