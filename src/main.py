import os

from file_handler import *
from data_processing import *
from api_handler import *
from report_generator import *


# Find project root directory dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths safely (NO hardcoding)
DATA_PATH = os.path.join(BASE_DIR, "data", "sales_data.txt")
ENRICHED_PATH = os.path.join(BASE_DIR, "output", "enriched_sales_data.txt")
REPORT_PATH = os.path.join(BASE_DIR, "output", "sales_report.txt")


def main():
    print("SALES ANALYTICS SYSTEM")

    # Read and parse sales data
    lines = read_sales_data(DATA_PATH)
    transactions = parse_transactions(lines)

    # Validate data
    valid, invalid, summary = validate_and_filter(transactions)
    print("Validation Summary:", summary)

    # API integration
    products = fetch_all_products()
    mapping = create_product_mapping(products)

    # Enrich data
    enriched = enrich_sales_data(valid, mapping)

    # Save outputs
    save_enriched_data(enriched, ENRICHED_PATH)
    generate_sales_report(enriched, REPORT_PATH)

    print("Process Completed")


if __name__ == "__main__":
    main()
