"""Automated test suite for finance_calculator.py."""

from unittest.mock import patch
from finance_calculator import (
    get_validated_float,
    calculate_finances,
    calculate_health_score,
    format_currency,
    generate_report,
)


# ─── Test: format_currency (Indian formatting) ────────────────
def test_format_currency():
    """Test Indian number formatting for several key values."""
    print("── format_currency ──────────────────────────")
    cases = [
        (100000,   "₹1,00,000.00"),
        (1200000,  "₹12,00,000.00"),
        (10000000, "₹1,00,00,000.00"),
        (999,      "₹999.00"),
        (1000,     "₹1,000.00"),
    ]
    for amount, expected in cases:
        result = format_currency(amount)
        status = "✅ PASS" if result == expected else f"❌ FAIL (got {result})"
        print(f"  format_currency({amount:>10}) = {result:<20} {status}")


# ─── Test: calculate_finances ─────────────────────────────────
def test_calculate_finances():
    """Test the 9 financial calculations with known inputs."""
    print("\n── calculate_finances ───────────────────────")
    data = calculate_finances(
        annual_salary=1_200_000,  # ₹12 LPA
        tax_percent=20,
        monthly_rent=15_000,
        savings_percent=20,
    )
    expected = {
        "monthly_salary":   100_000.0,
        "monthly_tax":       20_000.0,
        "net_salary":        80_000.0,
        "savings_amount":    16_000.0,
        "disposable_income": 49_000.0,
        "rent_ratio":        18.75,
        "annual_tax":       240_000.0,
        "annual_savings":   192_000.0,
        "annual_rent":      180_000.0,
    }
    all_pass = True
    for key, exp_val in expected.items():
        got = data[key]
        ok = abs(got - exp_val) < 0.01
        status = "✅ PASS" if ok else f"❌ FAIL (expected {exp_val}, got {got})"
        print(f"  {key:<22} = {got:>12.2f}   {status}")
        if not ok:
            all_pass = False
    return all_pass


# ─── Test: calculate_health_score ────────────────────────────
def test_health_score():
    """Test health score tiers with boundary values."""
    print("\n── calculate_health_score ───────────────────")
    cases = [
        # (rent_ratio, savings_pct, disposable_pct, description)
        (18.75, 20, 40, "Excellent scenario"),
        (35,    10, 20, "Average scenario"),
        (50,     5,  5, "Poor scenario"),
    ]
    for rent, sav, disp, desc in cases:
        score = calculate_health_score(rent, sav, disp)
        if score >= 75:
            tier = "🟢 Excellent"
        elif score >= 50:
            tier = "🟡 Average"
        else:
            tier = "🔴 Needs Improvement"
        print(f"  {desc:<22}  score={score:>3}/100  {tier}")


# ─── Test: get_validated_float ────────────────────────────────
def test_validated_float():
    """Test input validation: invalid then valid input sequences."""
    print("\n── get_validated_float ──────────────────────")

    # Should reject 'abc', then -5 (<=0), then accept 50000
    with patch("builtins.input", side_effect=["abc", "-5", "50000"]):
        result = get_validated_float("Salary: ", min_value=0)
    status = "✅ PASS" if result == 50000.0 else f"❌ FAIL (got {result})"
    print(f"  invalid → negative → valid : {result}  {status}")

    # Should reject 90 (>max 50), then accept 20
    with patch("builtins.input", side_effect=["90", "20"]):
        result = get_validated_float("Tax %: ", min_value=-1, max_value=50)
    status = "✅ PASS" if result == 20.0 else f"❌ FAIL (got {result})"
    print(f"  over-max → valid           : {result}  {status}")


# ─── Test: full generate_report (end-to-end) ─────────────────
def test_generate_report():
    """Run a full end-to-end report generation."""
    print("\n── generate_report (end-to-end) ─────────────")
    data = calculate_finances(1_200_000, 20, 15_000, 20)
    data["monthly_rent"] = 15_000
    generate_report(data, savings_percent=20, tax_percent=20)


# ─── Run all tests ────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 52)
    print("    FINANCE CALCULATOR — TEST SUITE")
    print("=" * 52)

    test_format_currency()
    all_calcs_pass = test_calculate_finances()
    test_health_score()
    test_validated_float()
    test_generate_report()

    print("\n" + "=" * 52)
    result = "✅ ALL TESTS PASSED" if all_calcs_pass else "❌ SOME TESTS FAILED"
    print(f"  {result}")
    print("=" * 52)
