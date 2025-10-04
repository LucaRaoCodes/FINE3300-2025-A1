# exchange_rates.py
# Class to convert between currencies

class ExchangeRates:
    def __init__(self, rate_to_usd):
        """
        rate_to_usd: 1 unit of foreign currency in USD
        """
        self.rate_to_usd = rate_to_usd

    def to_usd(self, amount):
        return amount * self.rate_to_usd

    def from_usd(self, amount):
        return amount / self.rate_to_usd
