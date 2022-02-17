#1 Fizz Buzz
''''''
def fizz_buzz(value1, value2):
    """ Creates list of values in range between value1 and value2 including value2,
    then searches which ones can be divided by 3 and 5,
    then returns sum of those numbers

    :param a: int. First value
    :param b: int. Second value
    :return : sum of values divisible by 3 and 5 in range between value1 and value2 (value2 included)
    """
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


#2 Plural
def plural_form(value1, value2, value3, value4):
    """Return correct single or plural form of the word depending on number

    :param a: int, First value
    :param b: str, Second value
    :param c: str, Third value
    :param d: str, 4th value
    :result: correct plural (or single) form of the word fitting the number
    """
    if value1 == 11 or value1 == 12:
        result = value4
    elif str(value1)[-1] == '1':
        result = value2
    elif str(value1)[-1] == '2' or str(value1)[-1] == '3' or str(value1)[-1] == '4':
        result = value3
    else:
        result = value4

    return result    
        
print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))        




































