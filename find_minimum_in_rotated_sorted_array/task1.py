"""
問題描述：
以下為某個國家中銀行貸款後利率及付款的計算方式。

條件：
- 貸款金額：20,000,000 元
- 月利率：0.15%
- 還款期限：30 年(360 個月）

問題：
若要在 30 年內(360 個月）還完，每月最少需要還多少錢？
（最後一個月會少還一些）

"""

loan = 20000000
rate = 0.15 * 0.01
duration = 360

class FindMinPayment:
    def __init__(self, loan, rate, duration):
        self.rate = rate
        self.loan = loan
        self.duration = duration

    def can_pay_off(self, monthly_payment: int):
        remaining = loan

        for _ in range(duration):
            interest = remaining * self.rate
            remaining = remaining + interest - monthly_payment

            if remaining <= 0:
                return True, 0

        return False, remaining

    def min_payment_search(self):

        left = 0
        right = self.loan

        min_payment = right

        while right - left > 1:

            mid = left + (right - left) / 2
            can_pay, _ = self.can_pay_off(mid)

            if can_pay:
                min_payment = mid
                right = mid
            else:
                left = mid

        return min_payment
    
    def remaining_payment(self, min_payment):
        min_payment = self.min_payment_search()
        _, remaining = self.can_pay_off(min_payment)
        return remaining


find_min_payment = FindMinPayment(loan=loan, rate=rate, duration=duration)
min_monthly_payment = find_min_payment.min_payment_search()
remaining = find_min_payment.remaining_payment(min_monthly_payment)
print(f"Min monthly payment: {min_monthly_payment}")
print(f"remaining in final month: {remaining}")
            