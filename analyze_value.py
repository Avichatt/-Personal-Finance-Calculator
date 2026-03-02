def analyze_value(value) -> str:
    """Analyze any Python value and return a summary string."""
    value_type = type(value).__name__
    truthiness = bool(value)
    try:
        length = len(value)
    except TypeError:
        length = "N/A"
    return (
        f"Value: {value} | "
        f"Type: {value_type} | "
        f"Truthy: {truthiness} | "
        f"Length: {length}"
    )


if __name__ == "__main__":
    # Test it with different types:
    print(analyze_value(42))
    # Value: 42 | Type: int | Truthy: True | Length: N/A

    print(analyze_value("hello"))
    # Value: hello | Type: str | Truthy: True | Length: 5

    print(analyze_value([]))
    # Value: [] | Type: list | Truthy: False | Length: 0

    print(analyze_value(None))
    # Value: None | Type: NoneType | Truthy: False | Length: N/A
