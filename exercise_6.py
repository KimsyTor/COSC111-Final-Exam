data = [
    ("name", "age", "phone"),
    ("John", 25, 1234567890),
    ("Jane", 24, 9876543210),
    ("Doe", 26, 1234567890),
]


def list_to_dict(lst: list) -> list:
    """
    This function takes a list of tuples and returns a list of dictionary.
    list index 0 is considered as the key of all the elements in the list.

    example:
    list_to_dict([
        ("name", "age", "phone"),
        ("John", 25, "1234567890"),
        ("Jane", 24, "9876543210"),
        ("Doe", 26, "1234567890"),
    ])

    # Output
    [
        {"name": "John", "age": 25, "phone": "1234567890"},
        {"name": "Jane", "age": 24, "phone": "9876543210"},
        {"name": "Doe", "age": 26, "phone": "1234567890"}
    ]
    """
    ...

