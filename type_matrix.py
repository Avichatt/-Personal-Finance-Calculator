"""
Python Type Conversion Matrix
Day 7 PM Assignment - IIT Gandhinagar — Part D

AI PROMPT USED TO GENERATE THIS FILE:
"Generate a Python type conversion matrix showing what happens when converting
between int, float, str, bool, list, and tuple. Include valid conversions,
errors, edge cases, and examples. Format as a table."

Generated with: Claude (claude-3-5-sonnet) | Manually tested and extended.
Edge cases NOT covered by AI have been added below with the label [ADDED].
"""


def section(title: str) -> None:
    """Print a section header for the matrix output."""
    print(f"\n{'='*55}")
    print(f"  {title}")
    print("=" * 55)


def safe_convert(expression: str, func, *args):
    """Attempt a conversion and print PASS or ERROR result.

    Args:
        expression: Human-readable string of the conversion being tested.
        func: The conversion callable.
        *args: Arguments to pass to func.
    """
    try:
        result = func(*args)
        print(f"  {expression:<35} -> {result!r}")
    except (TypeError, ValueError) as exc:
        print(f"  {expression:<35} -> ERROR: {type(exc).__name__}: {exc}")


# ─── int conversions ───────────────────────────────────────────
section("int → other types")
safe_convert("int(42) to float   : float(42)", float, 42)
safe_convert("int(42) to str     : str(42)", str, 42)
safe_convert("int(1)  to bool    : bool(1)", bool, 1)
safe_convert("int(0)  to bool    : bool(0)", bool, 0)
safe_convert("int(42) to list    : list(42)", list, 42)  # [ADDED] TypeError
safe_convert("int(42) to tuple   : tuple(42)", tuple, 42)  # [ADDED] TypeError

# ─── float conversions ─────────────────────────────────────────
section("float → other types")
safe_convert("float(3.14) to int    : int(3.99)", int, 3.99)  # truncates, not rounds
safe_convert("float(3.14) to str    : str(3.14)", str, 3.14)
safe_convert("float(0.0)  to bool   : bool(0.0)", bool, 0.0)
safe_convert("float(3.14) to bool   : bool(3.14)", bool, 3.14)
safe_convert("float('inf')          : float('inf')", float, "inf")  # [ADDED] valid!
safe_convert("float('nan')          : float('nan')", float, "nan")  # [ADDED] valid!
safe_convert("float('1.23')         : float('1.23')", float, "1.23")
safe_convert("float('abc')          : float('abc')", float, "abc")  # ValueError

# ─── str conversions ───────────────────────────────────────────
section("str → other types")
safe_convert("str('42')   to int    : int('42')", int, "42")
safe_convert("str('3.14') to int    : int('3.14')", int, "3.14")  # ValueError
safe_convert("str('3.14') to float  : float('3.14')", float, "3.14")
safe_convert("str('True') to bool   : bool('True')", bool, "True")  # [ADDED] True!
safe_convert("str('')     to bool   : bool('')", bool, "")  # [ADDED] False
safe_convert(
    "str('abc')  to list   : list('abc')", list, "abc"
)  # [ADDED] ['a','b','c']
safe_convert(
    "str('abc')  to tuple  : tuple('abc')", tuple, "abc"
)  # [ADDED] ('a','b','c')

# ─── bool conversions ──────────────────────────────────────────
section("bool → other types")
safe_convert("bool(True)  to int    : int(True)", int, True)  # 1
safe_convert("bool(False) to int    : int(False)", int, False)  # 0
safe_convert("bool(True)  to float  : float(True)", float, True)  # 1.0
safe_convert("bool(True)  to str    : str(True)", str, True)
safe_convert("True + True + False   : arithmetic", int, True + True + False)  # 2

# ─── list conversions ──────────────────────────────────────────
section("list → other types")
safe_convert("list([1,2]) to tuple  : tuple([1,2])", tuple, [1, 2])
safe_convert("list([1,2]) to str    : str([1,2])", str, [1, 2])
safe_convert("list([])    to bool   : bool([])", bool, [])  # False
safe_convert("list([0])   to bool   : bool([0])", bool, [0])  # True! (non-empty)

# ─── tuple conversions ─────────────────────────────────────────
section("tuple → other types")
safe_convert("tuple((1,2)) to list  : list((1,2))", list, (1, 2))
safe_convert("tuple((1,2)) to str   : str((1,2))", str, (1, 2))
safe_convert("tuple(())    to bool  : bool(())", bool, ())  # False

# ─── None edge cases ───────────────────────────────────────────
section("None edge cases [ADDED]")
safe_convert("None to bool  : bool(None)", bool, None)  # False
safe_convert("None to str   : str(None)", str, None)  # 'None'
safe_convert("None to int   : int(None)", int, None)  # TypeError

# ─── Floating-point gotcha ─────────────────────────────────────
section("Floating-point precision gotcha [ADDED]")
print(f"  {'0.1 + 0.2 == 0.3':<35} -> {0.1 + 0.2 == 0.3}")  # False!
print(f"  {'0.1 + 0.2':<35} -> {0.1 + 0.2}")  # 0.30000000000000004

print("\n✅ Matrix complete. See evaluation.txt for AI evaluation.\n")
