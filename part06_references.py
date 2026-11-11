# Ahmad, Roll No: __________, 2026-11-11
"""References, copying and mutable defaults."""
import copy


def add_item(item: str, cart: list[str] | None = None) -> list[str]:
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def main() -> None:
    # Prediction: a becomes [1, 2, 3, 4], c is separate and gets 5.
    a = [1, 2, 3]
    b = a
    b.append(4)
    c = a.copy()
    c.append(5)
    print(a)
    print(a, c)
    print(a is b, a is c, a == a[:])
    print(add_item("milk"), add_item("bread"))
    classes = {"A": ["Ali", "Sara"]}
    shallow = copy.copy(classes)
    deep = copy.deepcopy(classes)
    shallow["A"].append("Hamza")
    deep["A"].append("Ayesha")
    print(classes, shallow, deep)


if __name__ == "__main__":
    main()
