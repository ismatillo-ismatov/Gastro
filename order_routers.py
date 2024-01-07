from fastapi import APIRouter

order_router = APIRouter(
    prefix='/order',
    tags=["Order"]
)

@order_router.get('/')
def hello():
    return {"detail":"hello"}