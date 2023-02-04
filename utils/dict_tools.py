# Test Dictionaries

example_math = {
    "plus":['math',3],
    "add":['math',3],
    "minus":['math',3],
    "subtract":['math',3],
    "times":['math',3]
}

example_media = {
    "play":['media',5],
    "pause":['media',6],
    "spotify":['media',4],
    "times":['media',2]
}

def intersection(lst_1, lst_2):
    '''Intersection of two lists'''
    lst_3 = [value for value in lst_1 if value in lst_2]
    return lst_3

def dict_update(dict_1,dict_2):
    '''Similar to dict_1.update(dict_2), but instead of
    replacing the old values that intersect, they are simply
    appended to the existing list:\n
    As an example:\n
    dict_1[key] = list_1,dict_2[key] = list_2,\n
    Whereas dict_1.update(dict_2) indexed for key reveals list_2\n
    This method's output would reveal [list_1,list_2]'''
    keys_1,keys_2 = dict_1.keys(),dict_2.keys()
    shared = intersection(keys_1,keys_2)
    for key in shared:
        dict_2.update({key:[dict_1[key],dict_2[key]]})
    dict_1.update(dict_2)
    return dict_1

def increment(dict_1, value_pair):
    """Takes a list of two entrys [key,value] and updates dictionary with {key,value+existing} for easy data collection"""
    if dict_1.get(value_pair[0]) == None:
        dict_1.update({value_pair[0]:value_pair[1]})
    else:
        dict_1.update({value_pair[0]:value_pair[1]+dict_1.get(value_pair[0])})
    return dict_1