# Ahmad, Roll No: __________, 2026-11-11
"""Variables, input and output examples."""


def main() -> None:
    name = input("Name: ")
    age = int(input("Age: "))
    student_class = input("Class: ")
    city = input("City: ")
    print("\n======== STUDENT CARD ========")
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"Class: {student_class}")
    print(f"City : {city}")
    print(type(name), type(age), type(student_class), type(city))

    item = input("\nItem name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    subtotal = price * quantity
    discount = subtotal * 0.05
    tax = (subtotal - discount) * 0.17
    print(f"Subtotal: Rs {subtotal:.2f}")
    print(f"Discount: Rs {discount:.2f}")
    print(f"Tax: Rs {tax:.2f}")
    print(f"Total: Rs {subtotal - discount + tax:.2f}")
    print(f"{item}: {quantity}")


if __name__ == "__main__":
    main()
