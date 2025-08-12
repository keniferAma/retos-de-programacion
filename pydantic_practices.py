from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    product_name: str
    product_price: int
    product_amount: int

class ProductList(BaseModel):
    products: List[Product]

    def as_dict(self):
        return {product.product_name: product.product_price for product in self.products}


bunuelo = Product(product_name='bunuelo', product_price=1000, product_amount=1)
empanada = Product(product_name='empanada', product_price=2500, product_amount=2)


first_order = ProductList(products=[bunuelo, empanada])

print(first_order.model_dump().get('products'))
print(first_order.__dict__)
