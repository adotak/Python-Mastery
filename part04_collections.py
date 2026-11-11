# Ahmad, Roll No: __________, 2026-11-11
"""Lists, dictionaries, tuples and sets."""


def shopping_list() -> list[str]:
    items = ["milk", "bread", "eggs"]
    items.append("tea")
    items.remove("bread")
    items.sort()
    return items


def class_result() -> tuple[dict[str, tuple[int, float]], str, set[str]]:
    marks = {
        "Ali": [80, 72, 91], "Sara": [95, 88, 90], "Hamza": [65, 70, 61],
        "Ayesha": [39, 55, 60], "Bilal": [30, 45, 50],
    }
    results = {name: (sum(values), sum(values) / len(values)) for name, values in marks.items()}
    topper = max(results, key=lambda name: results[name][1])
    below_40 = {name for name, values in marks.items() if any(mark < 40 for mark in values)}
    return results, topper, below_40


def phone_book() -> None:
    contacts = {"Ali": "03000000001", "Sara": "03000000002", "Hamza": "03000000003",
                "Ayesha": "03000000004", "Bilal": "03000000005"}
    while True:
        choice = input("1 add, 2 search, 3 delete, 4 show all, 5 exit: ")
        if choice == "1":
            contacts[input("Name: ")] = input("Number: ")
        elif choice == "2":
            print(contacts.get(input("Name: "), "Not found"))
        elif choice == "3":
            contacts.pop(input("Name: "), None)
        elif choice == "4":
            for name, number in contacts.items():
                print(name, number)
        elif choice == "5":
            return


if __name__ == "__main__":
    for number, item in enumerate(shopping_list(), 1):
        print(number, item)
    print(class_result())
