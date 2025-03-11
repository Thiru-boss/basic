numbers = (1,2,3,4,5,6,7,8,9,10)

even_num = ()
odd_num = ()
sum_even = 0
sum_odd = 0
for i in numbers:
    if (i % 2 == 0):
        even_num = even_num + (i,)
        sum_even = sum_even + (i)

    else:
        odd_num = odd_num + (i,)
        sum_odd = sum_odd + (i)


print("even_num:", even_num)
print("sum_of_even:", sum_even)
print("odd_num:", odd_num)
print("sum_of_odd:", sum_odd)