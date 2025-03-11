num = int(input('Enter number'))

binary = ""
while num > 0:
    rem = str(num % 2)
    binary = rem + binary
    num = num // 2

print('Binary:', binary)