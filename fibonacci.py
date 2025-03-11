n = int(input('Enter nember'))
a = 0
b = 1
c = b
count = 1

if a == 0:
    print(a)
while count <= n:
    print(c)
    count = count + 1
    a, b = b, c
    c = a + b
print()