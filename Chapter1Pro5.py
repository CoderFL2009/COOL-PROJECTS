""""

Input: purchase price
Constants:
annual interest rate = 12%
downpayment = 10% of purchase price
Monthly payment = 5% of purchase price

"""
ANNUAL_RATE = .12
MONTHLY_RATE = ANNUAL_RATE/12

purchasePrice = float(input("Enter Purchase Price: "))

downPayment = purchasePrice * .1
purchasePrice = purchasePrice - downPayment

monthlyPayment = 0.05 * purchasePrice
month = 1
balance = purchasePrice
print("Month  Starting Balance  InterestToPay  PrincipalToPay      Payment          Remaining")
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * MONTHLY_RATE
    principal = monthlyPayment - interest
    remaining = balance - principal
    print("%2d%15.2f%15.2f%17.2f%17.2f.2%17.2f" % (month, balance, interest, principal, monthlyPayment, remaining))
    balance = remaining
    month+=1