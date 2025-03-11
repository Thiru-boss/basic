values = [88,25,65,48,71]

min_value = values[0]
max_value = values[0]

for num in values:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print('Minimum_no:', min_value)
print('Maximum_no:', max_value)