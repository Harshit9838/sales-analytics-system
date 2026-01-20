import os


def generate_sales_report(transactions, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    total_revenue = sum(
        t["Quantity"] * t["UnitPrice"] for t in transactions
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("SALES ANALYTICS REPORT\n")
        file.write("=====================\n\n")
        file.write(f"Total Revenue: {total_revenue}\n")
        file.write(f"Total Transactions: {len(transactions)}\n")
