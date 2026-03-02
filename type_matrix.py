"""
Python Type Conversion Matrix
Day 7 PM Assignment - Part D

AI Prompt used:
  "Generate a Python type conversion matrix showing what happens when
   converting between int, float, str, bool, list, and tuple.
   Include valid conversions, errors, edge cases, and examples."
"""


def demonstrate_conversions() -> None:
    """Demonstrate all key type conversions with outputs and edge cases."""
    print("=" * 56)
    print("PYTHON TYPE CONVERSION MATRIX")
    print("=" * 56)

    print("\n--- int() ---")
    print(f"int(3.99)         = {int(3.99)}")  # 3 — truncates
    print(f"int(True)         = {int(True)}")  # 1
    print(f"int(False)        = {int(False)}")  # 0
    print(f"int('42')         = {int('42')}")
    try:
        int("abc")
    except ValueError as e:
        print(f"int('abc')        → ValueError: {e}")
    try:
        int([1, 2])
    except TypeError as e:
        print(f"int([1,2])        → TypeError: {e}")

    print("\n--- float() ---")
    print(f"float(5)          = {float(5)}")  # 5.0
    print(f"float('3.14')     = {float('3.14')}")
    print(f"float(True)       = {float(True)}")  # 1.0
    print(f"float('inf')      = {float('inf')}")
    print(f"float('nan')      = {float('nan')}")

    print("\n--- str() ---")
    print(f"str(42)           = '{str(42)}'")
    print(f"str(True)         = '{str(True)}'")
    print(f"str([1,2,3])      = '{str([1,2,3])}'")

    print("\n--- bool() ---")
    print(f"bool(0)           = {bool(0)}")
    print(f"bool(1)           = {bool(1)}")
    print(f"bool('')          = {bool('')}")
    print(f"bool('False')     = {bool('False')}")
    print(f"bool([])          = {bool([])}")
    print(f"bool(None)        = {bool(None)}")

    print("\n--- list() ---")
    print(f"list('abc')       = {list('abc')}")  # ['a','b','c'] — splits chars!
    print(f"list((1,2,3))     = {list((1,2,3))}")
    try:
        list(5)
    except TypeError as e:
        print(f"list(5)          → TypeError: {e}")

    print("\n--- tuple() ---")
    print(f"tuple('abc')      = {tuple('abc')}")
    print(f"tuple([1,2,3])    = {tuple([1,2,3])}")

    print("\n--- Float precision gotcha ---")
    print(f"0.1+0.2 == 0.3   → {0.1+0.2 == 0.3}")  # False!
    print(f"0.1+0.2          → {0.1+0.2}")
    print("=" * 56)


if __name__ == "__main__":
    demonstrate_conversions()
