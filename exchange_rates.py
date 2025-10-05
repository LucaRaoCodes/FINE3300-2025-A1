# exchange_rates.py
# FINE3300 - Assignment 1
# Part 2: Exchange Rates
import csv

class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.exchange_rate = None
        self._load_latest_rate()

    def _load_latest_rate(self):
        """Reads the CSV and gets the latest USD/CAD rate from the last row."""
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            latest_row = rows[-1]  # last row = most recent
            self.exchange_rate = float(latest_row['USD/CAD'])  # make sure column name matches CSV

    def convert(self, amount, from_currency, to_currency):
        """Converts between USD and CAD."""
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.exchange_rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.exchange_rate
        else:
            raise ValueError("Only USD <-> CAD conversions are supported.")

# --- Interactive test ---
if __name__ == "__main__":
    converter = ExchangeRates("BankOfCanadaExchangeRates.csv")

    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (USD or CAD): ").upper()
    to_currency = input("To currency (USD or CAD): ").upper()

    converted = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")

