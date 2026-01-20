import requests


def fetch_all_products():
    try:
        response = requests.get("https://dummyjson.com/products")
        return response.json().get("products", [])
    except Exception as e:
        print("API Error:", e)
        return []


def create_product_mapping(products):
    return {p["title"]: p for p in products}


def enrich_sales_data(transactions, mapping):
    enriched = []

    for t in transactions:
        product = mapping.get(t["ProductName"])
        t["API_Match"] = product is not None

        if product:
            t["API_Category"] = product["category"]
            t["API_Brand"] = product["brand"]
            t["API_Rating"] = product["rating"]

        enriched.append(t)

    return enriched
