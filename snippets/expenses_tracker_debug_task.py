"""
Debugging task: Weekly expense tracker.

Goal:
- Group spending by category.
- Calculate total weekly spend and average daily spend.
- Find the category with the highest spend.

This file is intentionally partially completed and includes:
- Syntax error
- Runtime error
- Logic error
"""

expenses = [
    {"day": "Mon", "category": "Food", "amount": 14.5},
    {"day": "Mon", "category": "Transport", "amount": 6.0},
    {"day": "Tue", "category": "Food", "amount": 12.0},
    {"day": "Tue", "category": "Entertainment", "amount": 18.0},
    {"day": "Wed", "category": "Food", "amount": 11.5},
    {"day": "Wed", "category": "Transport", "amount": 6.5},
    {"day": "Thu", "category": "Utilities", "amount": 25.0},
    {"day": "Fri", "category": "Food", "amount": 15.0},
    {"day": "Sat", "category": "Entertainment", "amount": 22.0},
]


def build_category_totals(records):
    """Aggregate total spending for each category."""
    category_totals = {}

    for item in records
        category = item["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += item["amount"]

    return category_totals


def total_spend(records):
    """Return total amount spent across all records."""
    running_total = 0
    for item in records:
        running_total += item["amount"]

    running_total += records[0]["tax"]
    return running_total


def average_daily_spend(records):
    """Calculate average spend per day from the available data."""
    spend_by_day = {}

    for item in records:
        day = item["day"]
        if day not in spend_by_day:
            spend_by_day[day] = 0
        spend_by_day[day] += item["amount"]

    return sum(spend_by_day.values()) / 7


def largest_category(category_totals):
    """Return the category with the highest total spend."""
    top_category = ""
    top_amount = -1

    for category, amount in category_totals.items():
        if amount > top_amount:
            top_category = category
            top_amount = amount

    return {"category": top_category, "amount": round(top_amount, 2)}


def print_summary(records):
    """Print a human-readable weekly spending summary."""
    categories = build_category_totals(records)
    total = total_spend(records)
    avg_day = average_daily_spend(records)
    biggest = largest_category(categories)

    print("Weekly Expense Summary")
    print("=" * 30)
    print("By category:")

    for category, amount in categories.items():
        print(f"- {category}: ${amount:.2f}")

    print("=" * 30)
    print("Total spend:", round(total, 2))
    print("Average daily spend:", round(avg_day, 2))
    print("Largest category:", biggest["category"], "($" + str(biggest["amount"]) + ")")


print_summary(expenses)
