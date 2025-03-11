
n= 135
rev = 0

while(n != 0):
    rem = n % 10
    n = n//10

    # print(n)
    rev = rev * 10 + rem
print(rev)