import os
import utils.dict_tools

workingDir = os.path.dirname(os.path.realpath(__file__))+os.path.sep

with open(workingDir+"modules.txt",'r') as file:
    modules_enum = file.readlines()

""" 
Example Dictionaries
example = {
    word [ intent , confidence ]
}
Confidence is on a 0 - 9 scale
9 is most confident, 0 is least 
"""

command_hints = {}

print('-----===== Importing {} Modules =====-----'.format(len(modules_enum)))
for module in modules_enum:
    print('[INFO] Imported {} module'.format(module[:-1]))
    exec('import modules.{}'.format(module[:-1]))
    utils.dict_tools.dict_update(command_hints,eval('modules.{}.vocab'.format(module[:-1])))

recognized_words = command_hints.keys()

print('[INFO] {} words in vocabulary'.format(len(recognized_words)))

def recognize(string):
    tally = {}
    for word in string.split():
        if word in recognized_words:
            print(word)
            if type(command_hints[word][0]) == list:
                for entry in command_hints[word]:
                    utils.dict_tools.increment(tally,entry)
            else:
                utils.dict_tools.increment(tally,command_hints[word])

    print(tally)
    intent = max(tally,key=tally.get)

    exec("modules.{}.parse('{}')".format(intent,string))

while True:
    recognize(str(input()))
