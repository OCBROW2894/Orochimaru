
def invest(amount, rate, years):
    interest = (amount * (rate/100))
    amount = amount + interest
    return amount


balance = float(input("Enter your capital: "))
rate_p_a = float(input("Enter the annual percentage rate: "))
period = float(input("Number of Cycles: "))

start = 1

while start <= period :
    start = start + 1
    balance = invest(balance, rate_p_a, period)
    print(f"year {start - 1}: ${balance:,.2f}")

