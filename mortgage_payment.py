# mortgage_payment.py
# FINE3300 - Assignment 1
# Part 1: Mortgage Payments
# Author: Luca Rao

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

# --- Interactive user input and formatted output ---
if __name__ == "__main__":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter quoted annual rate (e.g., 5.5 for 5.5%): ")) / 100
    years = int(input("Enter amortization period in years: "))

    mortgage = MortgagePayment(rate, years)
    monthly, semi_monthly, bi_weekly, weekly, acc_bi_weekly, acc_weekly = mortgage.payments(principal)

    print(f"Monthly Payment: ${monthly}")
    print(f"Semi-monthly Payment: ${semi_monthly}")
    print(f"Bi-weekly Payment: ${bi_weekly}")
    print(f"Weekly Payment: ${weekly}")
    print(f"Rapid Bi-weekly Payment: ${acc_bi_weekly}")
    print(f"Rapid Weekly Payment: ${acc_weekly}")

