from typing import Dict
from collections import defaultdict

products_prices: Dict[str, int] = {
    "empanada": 2500, "bunuelo": 1000, "tinto_o_perico": 1200, 
    "cafe": 1700, "avena": 2000, "pastel": 4000, "gaseosa_o_malta_personal": 3000,
    "gaseosa_o_malta_mini": 1500
}

def sum_products(
    empanada_quantity: int = 0, bunuelo_quantity: int = 0, tinto_o_perico_quantity: int = 0,
    cafe_quantity: int = 0, avena_quantity: int = 0, pastel_quantity: int = 0, 
    gaseosa_o_malta_personal_quantity: int = 0, gaseosa_o_malta_mini_quantity: int = 0
) -> int:
    products = defaultdict(int, {
        "empanada": empanada_quantity, "bunuelo": bunuelo_quantity, "tinto_o_perico": tinto_o_perico_quantity, 
        "cafe": cafe_quantity, "avena": avena_quantity, "pastel": pastel_quantity, 
        "gaseosa_o_malta_personal": gaseosa_o_malta_personal_quantity, "gaseosa_o_malta_mini": gaseosa_o_malta_mini_quantity
    })

    total = sum(
        value * products_prices[product] for product, value in products.items()
    )
    return total

print(sum_products(empanada_quantity=5, bunuelo_quantity=4, cafe_quantity=2))

