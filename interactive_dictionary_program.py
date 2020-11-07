import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json", "r"))
dict_words = list(data.keys())
output = ''

def translate(w):
    if w.lower() in data:
        output = data[w.lower()]
    elif w.title() in data:
        output = data[w.title()]
    elif w.upper in data:
        output = data[w.upper()]
    else:
        
        try:
            closest_match = get_close_matches(w, data.keys())[0]
            prompt = input(f'Sorry. Your word was not found. Did you mean {closest_match}? \nInput y for yes.\nInput n for no.\nInput:  ')
            
            if prompt == 'y':
                return data[closest_match]
                
            elif prompt == 'n':
                return 'Sorry. No definition for your word. Double check and try again. '
                
            else:
                return 'Invalid input. Only valid inputs there are y and n. '
                
        except:
            return "Sorry. No definition for your word. It doesn't even come close to making sense. Have sense. MUMU!!! "
                
    for item in output:
        print(item)            
word = input("Please enter a word to obtain the definition(s):  ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

            

