"""
Personal Finance Calculator
Day 7 PM Assignment - IIT Gandhinagar

Calculates monthly/annual financial breakdown with Indian number formatting,
a financial health score, and full input validation.
"""

from typing import Dict


def get_validated_float(
    prompt: str, min_value: float, max_value: float = None
) -> float:
    """Get validated float input within a given range.

    Args:
        prompt: The input prompt displayed to the user.
        min_value: The value must be strictly greater than this.
        max_value: Optional upper bound (inclusive).

    Returns:
        A validated float value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= min_value:
                print(f"Value must be greater than {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be <= {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def format_currency(amount: float) -> str:
    """Format a number using the Indian numbering system (lakhs/crores).

    Examples:
        100000   -> ₹1,00,000.00
        1200000  -> ₹12,00,000.00
        10000000 -> ₹1,00,00,000.00

    Args:
        amount: The monetary value to format.

    Returns:
        A string with the ₹ symbol and Indian-style commas.
    """
    s = f"{amount:,.2f}"
    parts = s.split(".")
    integer_part = parts[0].replace(",", "")
    if len(integer_part) > 3:
        last_three = integer_part[-3:]
        remaining = integer_part[:-3]
        groups = [remaining[max(i - 2, 0) : i] for i in range(len(remaining), 0, -2)][
            ::-1
        ]
        remaining = ",".join(groups)
        formatted = remaining + "," + last_three
    else:
        formatted = integer_part
    return f"₹{formatted}.{parts[1]}"


def calculate_health_score(
    rent_ratio: float, savings_percent: float, disposable_percent: float
) -> int:
    """Calculate a financial health score from 0 to 100.

    Scoring pillars:
        - Rent ratio  : < 30% → 30 pts | 30–40% → 20 pts | >= 40% → 10 pts
        - Savings %   : up to 30 pts (capped at 30)
        - Disposable %: up to 40 pts (capped at 40)

    Args:
        rent_ratio: Rent as a percentage of net salary.
        savings_percent: Savings as a percentage of net salary.
        disposable_percent: Disposable income as a percentage of net salary.

    Returns:
        An integer score between 0 and 100.
    """
    score = 0
    if rent_ratio < 30:
        score += 30
    elif rent_ratio < 40:
        score += 20
    else:
        score += 10
    score += min(savings_percent, 30)
    score += min(disposable_percent, 40)
    return min(int(score), 100)


def calculate_finances(
    annual_salary: float,
    tax_percent: float,
    monthly_rent: float,
    savings_percent: float,
) -> Dict[str, float]:
    """Perform all 9 financial calculations and return as a dictionary.

    Args:
        annual_salary: Gross annual salary in rupees.
        tax_percent: Tax rate as a percentage (0–50).
        monthly_rent: Monthly rent expense in rupees.
        savings_percent: Savings rate as a percentage of net salary (0–100).

    Returns:
        A dictionary containing all computed financial metrics.
    """
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax
    savings_amount = net_salary * (savings_percent / 100)
    disposable_income = net_salary - monthly_rent - savings_amount
    rent_ratio = (monthly_rent / net_salary) * 100
    annual_tax = monthly_tax * 12
    annual_savings = savings_amount * 12
    annual_rent = monthly_rent * 12
    disposable_percent = (disposable_income / net_salary) * 100

    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "rent_ratio": rent_ratio,
        "annual_tax": annual_tax,
        "annual_savings": annual_savings,
        "annual_rent": annual_rent,
        "disposable_percent": disposable_percent,
    }


def generate_report(
    data: Dict[str, float], savings_percent: float, tax_percent: float
) -> None:
    """Print the full formatted financial report to the console.

    Args:
        data: Dictionary of computed financial values from calculate_finances().
        savings_percent: The user-entered savings percentage (for health score).
        tax_percent: The user-entered tax percentage (for display).
    """
    health_score = calculate_health_score(
        data["rent_ratio"], savings_percent, data["disposable_percent"]
    )

    # Determine health tier label
    if health_score >= 75:
        tier = "🟢 Excellent"
    elif health_score >= 50:
        tier = "🟡 Average"
    else:
        tier = "🔴 Needs Improvement"

    print("\n" + "=" * 52)
    print("       PERSONAL FINANCE REPORT")
    print("=" * 52)

    print("\n📅  MONTHLY BREAKDOWN")
    print("-" * 52)
    print(f"  Gross Salary     : {format_currency(data['monthly_salary'])}")
    print(
        f"  Tax ({tax_percent:.1f}%)        : -{format_currency(data['monthly_tax'])}"
    )
    print(f"  Net Salary       : {format_currency(data['net_salary'])}")
    print(
        f"  Rent             : -{format_currency(data['monthly_rent'] if 'monthly_rent' not in data else data.get('monthly_rent', 0))}"
    )
    print(
        f"  Savings ({savings_percent:.1f}%)    : -{format_currency(data['savings_amount'])}"
    )
    print(f"  Disposable       : {format_currency(data['disposable_income'])}")
    print(f"  Rent-to-Income   : {data['rent_ratio']:.1f}%")

    print("\n📆  ANNUAL PROJECTION")
    print("-" * 52)
    print(f"  Annual Tax       : {format_currency(data['annual_tax'])}")
    print(f"  Annual Rent      : {format_currency(data['annual_rent'])}")
    print(f"  Annual Savings   : {format_currency(data['annual_savings'])}")

    print("\n💯  FINANCIAL HEALTH SCORE")
    print("-" * 52)
    print(f"  Score            : {health_score}/100")
    print(f"  Rating           : {tier}")
    print("=" * 52 + "\n")


def main() -> None:
    """Collect user inputs and run the full financial analysis."""
    print("\n=== Personal Finance Calculator ===\n")

    annual_salary = get_validated_float("Enter your annual salary (₹): ", min_value=0)
    tax_percent = get_validated_float(
        "Enter your tax rate (%): ", min_value=-1, max_value=50
    )
    monthly_rent = get_validated_float("Enter your monthly rent (₹): ", min_value=0)
    savings_percent = get_validated_float(
        "Enter your savings rate (% of net salary): ", min_value=-1, max_value=100
    )

    results = calculate_finances(
        annual_salary, tax_percent, monthly_rent, savings_percent
    )
    # Store monthly_rent in results for report use
    results["monthly_rent"] = monthly_rent

    generate_report(results, savings_percent, tax_percent)


if __name__ == "__main__":
    main()
