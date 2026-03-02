"""Q3 - Fixed buggy code. Original had 4 issues."""


def get_user_info() -> None:
    """Collect name and age, determine adult/minor status."""
    name = input("Name: ")
    age = int(input("Age: "))  # Bug 1 fixed: missing int()

    if age >= 18:  # Bug 2 fixed: indentation
        status = "Adult"
    else:
        status = "Minor"

    # Bug 3 fixed: {name} not {age} in first f-string
    print(f"{name} is {age} years old and is a {status}")
    print(f"In 5 years: {age + 5}")

    score = 85.5
    print(f"Score: {score:.0f}")  # Bug 4 fixed: .0 → .0f


if __name__ == "__main__":
    get_user_info()
