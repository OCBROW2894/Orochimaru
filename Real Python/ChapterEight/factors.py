"""
 Challenge: FindtheFactors of a Number
"""
def factors(num):
    for n in range(1, num + 1) :
        factor = num % n
        if factor == 0:
            print(f"{n} is a factor of {num}")
        n = n + 1
    return factor

number = int(input("Enter a positive integer: "))

factors(number)
