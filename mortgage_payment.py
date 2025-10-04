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
# mortgage_payment.py
# Class to calculate mortgage payments for multiple payment options

class MortgagePayment:
    def __init__(self, quoted_rate, amortization_years):
        """
        quoted_rate: annual mortgage rate as decimal (e.g., 0.055 for 5.5%)
        amortization_years: total years of mortgage
        """
        self.quoted_rate = quoted_rate
        self.amortization_years = amortization_years

    def _pva(self, r, n):
        """Present value of annuity factor"""
        return (1 - (1 + r) ** -n) / r

    def payments(self, principal):
        """
        Returns a tuple with payments in the order:
        monthly, semi-monthly, bi-weekly, weekly, accelerated bi-weekly, accelerated weekly
        """
        # Payment frequencies
        periods = {
            "monthly": 12,
            "semi_monthly": 24,
            "bi_weekly": 26,
            "weekly": 52
        }

        results = {}

        for key, m in periods.items():
            # periodic rate for this frequency (semi-annual compounding)
            r_period = (1 + self.quoted_rate / 2) ** (2 / m) - 1
            n_periods = self.amortization_years * m
            results[key] = principal / self._pva(r_period, n_periods)

        # Accelerated payments
        results["acc_bi_weekly"] = results["monthly"] / 2
        results["acc_weekly"] = results["monthly"] / 4

        return (
            round(results["monthly"], 2),
            round(results["semi_monthly"], 2),
            round(results["bi_weekly"], 2),
            round(results["weekly"], 2),
            round(results["acc_bi_weekly"], 2),
            round(results["acc_weekly"], 2)
        )
if __name__ == "__main__":
    mortgage = MortgagePayment(0.055, 25)  # 5.5% rate, 25-year amortization
    principal = 100000
    print(mortgage.payments(principal))
