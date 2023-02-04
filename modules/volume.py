'''
This module can change the volume on windows hosts courtesy of linearWinVolume
'''

import modules.number_parser
import utils.str_tools
import os

workingDir = os.path.dirname(os.path.realpath(__file__))+os.path.sep

vocab = {
    "raise":['volume',4],
    "lower":['volume',4],
    "volume":['volume',9],
    "to":['volume',3],
    "by":['volume',3],
    "percent":['volume',4],
    "mute":['volume',9],
    "maximum":['volume',2],
    "set":['volume',3],
}

'''
examples:
raise volume by 5
lower volume by 5 percent
set volume to 50 percent
set volume to 50
what is the volume
mute volume
mute
set volume to maximum
'''

numbers = modules.number_parser.digits_English.copy()
numbers.update(modules.number_parser.tens_English)

def vol_parse(string):
    index = 0
    grammer_flag = None
    for word in string:
        index += 1
        if word == 'by':
            grammer_flag = 'by'
            break
        elif word == 'to':
            grammer_flag = 'to'
            break
    vol_value = utils.str_tools.filter_for_numbers(' '.join(string[index:]))
    return [modules.number_parser.parse_number(vol_value),grammer_flag]

def parse(text):
    print('parsing!')
    try:
        phrase = text.split()
        if 'mute' in phrase:
            os.system('py "{}volume_daemon.py" set {}'.format(workingDir,0))
            # linearwinvolume.set_volume(0)
            return 1
        arguments = vol_parse(phrase)
        if 'to' in phrase:
            os.system('py "{}volume_daemon.py" set {}'.format(workingDir,arguments[0]))
            # linearwinvolume.set_volume(arguments[0])
        elif 'by' in phrase:
            if 'raise' in phrase:
                # linearwinvolume.change_volume(arguments[0])
                os.system('py "{}volume_daemon.py" change {}'.format(workingDir,arguments[0]))
            elif 'lower' in phrase:
                # linearwinvolume.change_volume(-arguments[0])
                os.system('py "{}volume_daemon.py" change -{}'.format(workingDir,arguments[0]))
        return 1
    except Exception as e:
        print(e)
        return 0
