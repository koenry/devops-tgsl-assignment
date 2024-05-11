from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class ServiceOrder(BaseModel):
    id: str | None = None # So that the user does not need to assign an ID
    description: str
    status: str

db: List[ServiceOrder] = []


@app.post('/serviceorders/', response_model=ServiceOrder)
def create_service_order(service_order: ServiceOrder):
    service_order.id = str(uuid4())  # Assign a unique ID
    db.append(service_order)
    return service_order


@app.get('/serviceorders/', response_model=List[ServiceOrder])
def get_service_orders():
    return db


@app.get('/serviceorders/{order_id}', response_model=ServiceOrder)
def get_service_order(order_id: str):
    for order in db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail='Service order not found')


@app.patch('/serviceorders/{order_id}', response_model=ServiceOrder)
def update_service_order(order_id: str, service_order: ServiceOrder):
    for order in db:
        if order.id == order_id:
            order.description = service_order.description if service_order.description else order.description
            order.status = service_order.status if service_order.status else order.status
            return order
    raise HTTPException(status_code=404, detail="Service order not found")


@app.delete('/serviceorders/{order_id}', status_code=204)
def delete_service_order(order_id: str):
    for index, order in enumerate(db):
        if order.id == order_id:
            del db[index]
            return
    raise HTTPException(status_code=404, detail="Service order not found")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
