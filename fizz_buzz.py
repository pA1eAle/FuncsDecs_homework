#Функция fizz_buzz
def fizz_buzz(a, b):
    result = 0
    list = []
    for i in range(a, b+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append(i)
    result = sum(list)    
    return result

print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))


#Функция plural_form
def plural_form(a, form1, form2, form3):
    result = ''
    n = list(str(a))
    if int(n[-1]) == 1:
        if len(n) >= 2:
            if int(n[-2]) == 1:
                result = form3
            else:
                result = form1
        else:
                result = form1           
    elif int(n[-1]) in range(2, 5):
        result = form2
    elif int(n[-1]) in range(5, 21):
        result = form3
    return result

print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))


#Декоратор html
def html(a, width=0, height=0, href=''):

    def decorator(decorated_function):

        def function_inside_decorator(input_value):
            
            result_decorated_function = f'<{a}>{decorated_function(input_value)}</{a}>'

            if width and height:
                result_decorated_function = f'<{a} width="{str(width)}" height="{str(height)}">{decorated_function(input_value)}</{a}>'
            elif width:
                result_decorated_function = f'<{a} width="{str(width)}">{decorated_function(input_value)}</{a}>'    
            elif height:
                result_decorated_function = f'<{a} height="{str(height)}">{decorated_function(input_value)}</{a}>'
                
            if href:
                result_decorated_function = f'<{a} href="{href}">{decorated_function(input_value)}</{a}>'              
            
            return result_decorated_function
    
        return function_inside_decorator
    
    return decorator


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))




   
    
