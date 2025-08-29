"""
Challenge: Track Your Investments
"""
def invest(amount, rate, years):
    start = 1
    while start <= years:
        start = start + 1
        interest = (amount * (rate/100))
        amount = amount + interest
        print(f"year {start - 1}: ${amount:,.2f}")
    return amount


balance = float(input("Enter your capital: "))
rate_p_a = float(input("Enter the annual percentage rate: "))
period = float(input("Number of Cycles: "))

invest(balance, rate_p_a, period)
