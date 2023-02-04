import math

digits_English = {
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'eleven':11,
    'twelve':12,
    'thirteen':13,
    'fourteen':14,
    'fifteen':15,
    'sixteen':16,
    'seventeen':17,
    'eighteen':18,
    'nineteen':19,
}

tens_English = {
    'twenty':2,
    'thirty':3,
    'forty':4,
    'fifty':5,
    'sixty':6,
    'seventy':7,
    'eighty':8,
    'ninety':9
}

magnitude_English = {
    'hundred':10**2,
    'thousand':10**3,
    'million':10**6
}

def parse_number(number_str):
    '''Returns amount of digits in a number string up to nine digits'''
    number,decimal,pi_flag,e_flag = 0,0,False,False
    number_place_values = ['','',''] # million, thousand, ones, thousandths
    if 'pi' in number_str:
        number_str = ''.join(number_str.split('pi'))
        pi_flag = True
    if ' e' in number_str:
        number_str = ''.join(number_str.split('e'))
        e_flag = True
    if 'point' in number_str:
        if number_str.startswith('point'):
            number_str = ' '+number_str
        if len(number_str.split(' point')) > 1:
            integer,decimal = number_str.split(' point')
        else:
            decimal = str(number_str.split(' point'))
            integer = '0'
        decimal = parse_number(decimal)
    elif 'dot' in number_str:
        if len(number_str.split(' dot')) > 1:
            integer,decimal = number_str.split(' dot')
        else:
            decimal = str(number_str.split(' dot'))
            integer = '0'
        decimal = parse_number(decimal)
    else:
        integer = number_str
    if 'million' in integer:
        millions = integer.split(' million')
        number_place_values[0],remaining_numbers = millions[0],''.join(millions[1:])[1:]
    else:
        remaining_numbers = integer
    if 'thousand' in remaining_numbers:
        thousands = remaining_numbers.split(' thousand')
        number_place_values[1],remaining_numbers = thousands[0],''.join(thousands[1:])[1:]
    else:
        remaining_numbers = integer if 'million' not in integer else remaining_numbers
    number_place_values[2] = remaining_numbers
    number += parse_place_values(number_place_values[0])*10**6
    number += parse_place_values(number_place_values[1])*10**3
    number += parse_place_values(number_place_values[2])
    if decimal != None:
        number = float(str(int(number))+'.'+str(int(decimal)))
    if pi_flag:
        number = number * math.pi if number != 0 else math.pi
    if e_flag:
        number = number * math.e if number != 0 else math.e
    return number

def parse_place_values(hundreds_str):
    number = 0
    hundreds_str = hundreds_str.split(' hundred')
    if len(hundreds_str) > 1:
        hundreds_place,remaining_numbers = hundreds_str[0],''.join(hundreds_str[1:])
        number += digits_English.get(hundreds_place)*100
    else:
        remaining_numbers = ''.join(hundreds_str)
    for i in remaining_numbers.split():
        if i in tens_English:
            number += tens_English.get(i)*10
        elif i in digits_English:
            number += digits_English.get(i)
        elif i == '':
            pass
        else:
            raise ValueError
    return number

# print(parse_number(input()))