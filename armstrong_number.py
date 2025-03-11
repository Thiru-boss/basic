n=int(input("enter any no"))
length = len(str(n))
check_n=n
armstrong=0
while n != 0:
    rem=n % 10
    n = n // 10
    armstrong=armstrong+(rem** length)

if(check_n == armstrong):
    print("yes - armstrong no")
else:
    print(" not an armstrong no")