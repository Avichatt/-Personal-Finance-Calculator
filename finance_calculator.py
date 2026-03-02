"""
Personal Finance Calculator
Day 7 PM Assignment - IIT Gandhinagar
"""

from typing import Dict


def get_validated_float(
    prompt: str, min_value: float, max_value: float = None
) -> float:
    """Get validated float input within a given range."""
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
    """Format amount in Indian numbering system (lakhs/crores).
    Example: 1200000 → ₹12,00,000.00
    """
    raw = f"{amount:,.2f}"
    parts = raw.split(".")
    integer_part = parts[0].replace(",", "")
    if len(integer_part) > 3:
        last_three = integer_part[-3:]
        remaining = integer_part[:-3]
        grouped = ",".join(
            [remaining[max(i - 2, 0) : i] for i in range(len(remaining), 0, -2)][::-1]
        )
        formatted = grouped + "," + last_three
    else:
        formatted = integer_part
    return f"₹{formatted}.{parts[1]}"


def calculate_finances(
    annual_salary: float,
    tax_percent: float,
    monthly_rent: float,
    savings_percent: float,
) -> Dict[str, float]:
    """Perform all financial calculations and return as a dictionary."""
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax
    savings_amount = net_salary * (savings_percent / 100)
    disposable_income = net_salary - monthly_rent - savings_amount
    rent_ratio = (monthly_rent / net_salary) * 100
    disposable_percent = (disposable_income / net_salary) * 100
    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "rent_ratio": rent_ratio,
        "disposable_percent": disposable_percent,
        "annual_tax": monthly_tax * 12,
        "annual_savings": savings_amount * 12,
        "annual_rent": monthly_rent * 12,
    }


def calculate_health_score(
    rent_ratio: float, savings_percent: float, disposable_percent: float
) -> int:
    """Return a financial health score from 0 to 100.

    Scoring breakdown:
      Rent discipline   : up to 30 pts
      Savings behaviour : up to 30 pts
      Disposable income : up to 40 pts
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


def generate_report(
    name: str,
    annual_salary: float,
    tax_percent: float,
    monthly_rent: float,
    savings_percent: float,
    data: Dict[str, float],
) -> None:
    """Generate and print the formatted financial summary report."""
    health = calculate_health_score(
        data["rent_ratio"], savings_percent, data["disposable_percent"]
    )
    print("═" * 44)
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("═" * 44)
    print(f"Employee        : {name}")
    print(f"Annual Salary   : {format_currency(annual_salary)}")
    print("─" * 44)
    print("Monthly Breakdown:")
    print(f"  Gross Salary  : {format_currency(data['monthly_salary'])}")
    print(f"  Tax ({tax_percent}%)      : {format_currency(data['monthly_tax'])}")
    print(f"  Net Salary    : {format_currency(data['net_salary'])}")
    print(
        f"  Rent          : {format_currency(monthly_rent)} ({data['rent_ratio']:.1f}% of net)"
    )
    print(f"  Savings ({savings_percent}%) : {format_currency(data['savings_amount'])}")
    print(f"  Disposable    : {format_currency(data['disposable_income'])}")
    print("─" * 44)
    print("Annual Projection:")
    print(f"  Total Tax     : {format_currency(data['annual_tax'])}")
    print(f"  Total Savings : {format_currency(data['annual_savings'])}")
    print(f"  Total Rent    : {format_currency(data['annual_rent'])}")
    print("─" * 44)
    print(f"Financial Health Score: {health}/100")
    print("═" * 44)


def main() -> None:
    """Main entry point — collect inputs and run the report."""
    name = input("Enter employee name: ")
    annual_salary = get_validated_float("Enter annual salary: ", 0)
    tax_percent = get_validated_float("Enter tax percentage (0-50): ", -1, 50)
    monthly_rent = get_validated_float("Enter monthly rent: ", 0)
    savings_percent = get_validated_float(
        "Enter savings goal percentage (0-100): ", -1, 100
    )
    data = calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent)
    generate_report(
        name, annual_salary, tax_percent, monthly_rent, savings_percent, data
    )


if __name__ == "__main__":
    main()
