'''math_parser is a basic scientific calculator and currently has feature parity with a cheap scientific calculator
it supports all basic math operations with natrual language input, and with numbers as big as 10^9
additionally, it also supports the three basic trigonometric functions, standard logarithms, raising numbers to the
power of two and three, and the constants pi and e

TODO:
- improve english to formula syntax to support more complex equations'''

from modules.number_parser import parse_number
from utils.str_tools import split_by_list
import math

vocab = {
    "plus":['math_parser',5],
    "add":['math_parser',5],
    "minus":['math_parser',5],
    "subtract":['math_parser',5],
    "negative":['math_parser',3],
    "times":['math_parser',5],
    "multiply":['math_parser',5],
    "over":['math_parser',3],
    "divide":['math_parser',5],
    "squared":['math_parser',5],
    "cubed":['math_parser',5],
    "log":['math_parser',3],
    "root":['math_parser',5],
    "sine":['math_parser',5],
    "cosine":['math_parser',5],
    "tangent":['math_parser',5]
}

transcription = 'cosine two pi plus sine zero point five pi'

ANGULAR_UNITS = 'rad'

operators = {
    "plus":'+',
    "add":'+',
    "minus":'-',
    "subtract":'-',
    "negative":' -',
    "times":'*',
    "multiply":'*',
    "over":'/',
    "divide":'/',
    "squared":'**2 ',
    "cubed":'**3',
    "log":'math.log(',
    "root":'math.sqrt('
}

trig_rad = {
    "sine":'math.sin(',
    "cosine":'math.cos(',
    "tangent":'math.tan('
}

trig_deg = {
    "sine":'math.sin(math.radians(',
    "cosine":'math.cos(math.radians(',
    "tangent":'math.tan(math.radians('
}

if ANGULAR_UNITS == 'deg':
    operators.update(trig_deg)
elif ANGULAR_UNITS == 'rad':
    operators.update(trig_rad)
else:
    print('trig not implemented')

def parse_equation(text):
    text = text.lower()
    text = split_by_list(text,list(operators.keys()))
    print(text)
    equation = ''
    close_var = 0

    for i in text:
        if i in operators:
            equation += operators[i]
            close_var = operators[i].count('(')
        else:
            equation += str(parse_number(i)) + ')'*close_var
    # print(equation)
    return eval(equation)

def parse(text):
    print(parse_equation(text))

# while True:
#     print(parse_equation(input()))