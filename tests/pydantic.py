from pydantic import BaseModel,ValidationError
from typing import Optional


class Product(BaseModel):
    id: int
    name: str
    volume: Optional[int] = 'Madafaka'


dict1 = {'id': "78", "name": 456, "volume": ["a","ba"]}

try:
    product = Product(**dict1)
except ValidationError as error:
    print(error.json())
