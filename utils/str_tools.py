test_list = ['plus', 'add', 'minus', 'subtract', 'negative', 'times', 'multiply', 'over', 'divide', 'squared', 'cubed', 'log', 'root', 'sine', 'cosine', 'tangent']
test_string = "two pi plus three point five minus four dot two times negative"

import modules.number_parser
numbers = modules.number_parser.digits_English.copy()
numbers.update(modules.number_parser.tens_English)

def in_list(string, values):
    if type(values) == list:
        for i in values:
            if i in string:
                return True
        return False
    else:
        return False

def split_by_list(string, seperators):
    '''Similar to the normal string.split() command, only instead of spliting at a single
    string delimiter, this version splits by all strings in the list seperators'''
    text = string.split()
    indexes = []
    for i in range(len(text)):
        if in_list(text[i],seperators):
            indexes.append(i)
    intermediate_values = []
    for i in range(len(indexes)):
        intermediate_values.append(" ".join(text[0 if i == 0 else indexes[i-1]+1:indexes[i]]))
    if len(indexes) == 0:
        return [string]
    intermediate_values.append(" ".join(text[indexes[-1]+1:]))
    keywords = []
    for i in indexes:
        keywords.append(text[i])
    for i in range(len(keywords)):
        intermediate_values.insert((i+1)*2-1,keywords[i])
    while "" in intermediate_values:
        intermediate_values.remove("")
        print("in while loop")
    return intermediate_values

def filter_for_numbers(string):
    '''Filters out any non number words and characters and returns a string that can be parsed by number_parser.py
    \nFor example: 'five percent twenty four' becomes 'five twenty four'
    '''
    phrase = string.split()
    for i in phrase:
        if i not in numbers:
            phrase.remove(i)
    return ' '.join(phrase)

# print(filter_for_numbers('five percent twenty four'))
# print(split_by_list('two point five',test_list))