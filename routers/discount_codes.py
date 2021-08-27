from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from utilities.code_generator import code_generator

router = APIRouter(
   prefix="/brands",
)

# Mock database with functions for reading and writing
mock_db = {"brands": {
   "shoez": {
      "discount_codes": [
         {
            "id": 1,
            "code": "aKc3s5",
            "claimed": False,
            "isActive": True,
         },
      ],
   },
}}
mock_db_id_counter = 2

def read_code(brand: str):
   for code in mock_db["brands"][brand]["discount_codes"]:
      if not code["claimed"]:
         code["claimed"] = True
         return code["code"]
   return None

def create_code(brand: str, code: str):
   global mock_db_id_counter
   discount_code = {
      "id": mock_db_id_counter,
      "code": code,
      "claimed": False,
      "isActive": True,
   }
   mock_db_id_counter += 1
   mock_db["brands"][brand]["discount_codes"].append(discount_code)

# Pydantic models for handling request bodies
class DiscountRequest(BaseModel):
   quantity: int

# Router functions for handling get and post
@router.get("/{brand}/discount-codes")
def read_discount(brand: str):
   if brand not in mock_db["brands"]:
      raise HTTPException(status_code=404, detail="Brand not found")

   code = read_code(brand)
   if not code:
      raise HTTPException(status_code=404, detail="No discount codes")

   return {"discount_code": code}

@router.post("/{brand}/discount-codes")
def create_discounts(brand: str, discountRequest: DiscountRequest):
   # Create a brand if it does not yet exist
   if brand not in mock_db["brands"]:
      mock_db["brands"][brand] = {"discount_codes": []}
   
   codes = []
   for code in code_generator(6, discountRequest.quantity):
      codes.append(code)
      create_code(brand, code)

   return {"discount-codes": codes}
