# mortgage_payment.py
# Class to calculate mortgage payments

class MortgagePayment:
    def __init__(self, principal, annual_rate, years):
        """
        principal: loan amount
        annual_rate: annual interest rate (as a decimal, e.g., 0.05 for 5%)
        years: term of mortgage in years
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def monthly_payment(self):
        """
        Calculates monthly mortgage payment
        """
        r = self.annual_rate / 12  # monthly interest rate
        n = self.years * 12        # total payments
        if r == 0:
            return self.principal / n
        return self.principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
