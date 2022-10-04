from decimal import Decimal

digit = Decimal(input('Enter a real number: '))
digit = digit.quantize(Decimal(input('Enter the required accuracy "0.0001":')))
print(digit)
