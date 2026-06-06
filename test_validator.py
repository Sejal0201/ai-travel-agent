from budget_validator import validate_budget

sample = """
Flights ₹4000
Hotel ₹12000
Food ₹5000
"""

print(
    validate_budget(sample)
)