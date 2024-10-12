import csv
from typing import Dict, List


def get_financial_transactions(path: str) -> List[Dict]:
    transactions = []
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Указываем ; как разделитель
        for row in reader:
            transactions.append(row)
            print(
                row["id"],
                row["state"],
                row["date"],
                row["amount"],
                row["currency_name"],
                row["currency_code"],
                row["from"],
                row["to"],
                row["description"],
            )
    return transactions


path = "transactions.csv"
transactions = get_financial_transactions(path)
