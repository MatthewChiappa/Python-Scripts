import math

balance = float(raw_input('What is the balance? '))
annualInterestRate = float(raw_input('What is the annual interest rate? '))
monthlyPaymentRate = float(raw_input('What is the monthly payment rate? '))
origBal = balance
total = 0

interestRate = annualInterestRate / 12.0

for month in range(1,13):
    minPay = monthlyPaymentRate * balance
    total += minPay
    unPaid = balance - minPay
    balance = unPaid + (interestRate * unPaid)
    print 'Month:', month
    print 'Minimum Monthly Payment:', math.ceil(minPay * 100) / 100
    print 'Remaining Balance:', math.ceil(balance * 100) / 100

print 'Total Paid:', math.ceil(total * 100) / 100
print 'Remaining balance:', math.ceil(balance * 100) / 100