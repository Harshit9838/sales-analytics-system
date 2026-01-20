def read_sales_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print("Error reading file:", e)
        return []


def parse_transactions(lines):
    transactions = []

    for line in lines[1:]:
        parts = line.split("|")
        if len(parts) != 8:
            continue
        try:
            transactions.append({
                "TransactionID": parts[0].strip(),
                "Date": parts[1].strip(),
                "ProductID": parts[2].strip(),
                "ProductName": parts[3].strip(),
                "Quantity": int(parts[4]),
                "UnitPrice": float(parts[5].replace(",", "")),
                "CustomerID": parts[6].strip(),
                "Region": parts[7].strip()
            })
        except:
            continue

    return transactions


def validate_and_filter(transactions):
    valid = []
    invalid = 0

    for t in transactions:
        if (
            t["Quantity"] > 0 and
            t["UnitPrice"] > 0 and
            t["TransactionID"].startswith("T") and
            t["ProductID"].startswith("P") and
            t["CustomerID"] and
            t["Region"]
        ):
            valid.append(t)
        else:
            invalid += 1

    summary = {
        "total_records": len(transactions),
        "invalid_records": invalid,
        "valid_records": len(valid)
    }

    return valid, invalid, summary
