def fizz_buzz(value1, value2):
    interval = []
    for value in range(value1, value2 + 1):
        interval.append(value)
        
    i = 0
    fizz_buzz_list = []
    while i < len(interval):
        value_checked = interval[i]
        if value_checked % 3 == 0 and value_checked % 5 == 0:
            fizz_buzz_list.append(value_checked)
            i += 1
        else:
            i += 1
                
    return sum(fizz_buzz_list)

print('0-3: ', fizz_buzz(0, 3))
print('0-5: ', fizz_buzz(0, 5))
print('15-15: ', fizz_buzz(15, 15))
print('1000-20000: ', fizz_buzz(1000, 20000))


