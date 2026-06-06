import re

def validate_budget(plan, user_budget):

    user_budget = int(user_budget)

    nums = re.findall(
        r"\d[\d,]*",
        plan
    )

    values = [
        int(x.replace(",",""))
        for x in nums
    ]

    extracted_total = max(
        values,
        default=0
    )

    if extracted_total <= user_budget:

        return "VALID"

    return "INVALID"