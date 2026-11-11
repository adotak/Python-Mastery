# Ahmad, Roll No: __________, 2026-11-11
"""Type hints and dataclasses."""
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass(order=True)
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list, compare=False)

    def __post_init__(self) -> None:
        if self.price < 0 or self.stock < 0:
            raise ValueError("Price and stock cannot be negative")


def save_products(products: list[Product], path: Path) -> None:
    path.write_text(json.dumps([asdict(product) for product in products], indent=2), encoding="utf-8")


def load_products(path: Path) -> list[Product]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Product(**item) for item in data]


if __name__ == "__main__":
    products = [Product("Pen", 50, 0), Product("Book", 300, 5), Product("Bag", 1200, 0),
                Product("Pencil", 20, 10), Product("Ruler", 80, 2)]
    print([product.name for product in products if product.stock == 0])
