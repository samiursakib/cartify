from fastapi import APIRouter

router = APIRouter(
  prefix="/products"
)

@router.get("/")
def get_products():
  return [{ "id": 1, "name": "Product 1" }, { "id": 2, "name": "Product 2" }]
