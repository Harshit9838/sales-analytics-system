def calculate_total_revenue(transactions):
    return sum(t["Quantity"] * t["UnitPrice"] for t in transactions)


def region_wise_sales(transactions):
    regions = {}
    total = calculate_total_revenue(transactions)

    for t in transactions:
        region = t["Region"]
        regions.setdefault(region, {"sales": 0, "transactions": 0})
        regions[region]["sales"] += t["Quantity"] * t["UnitPrice"]
        regions[region]["transactions"] += 1

    for r in regions:
        regions[r]["percentage"] = round(
            (regions[r]["sales"] / total) * 100, 2
        )

    return regions
