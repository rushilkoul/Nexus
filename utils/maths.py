import re
def evaluate(userinput):
    try:
       print()
       return str(eval(cleanInput(userinput)))
    except Exception as e:
        print(e)
        return "Sorry, I could not calculate that."


def cleanInput(userinput):
    _input = userinput

    if 'evaluate' in userinput:
        _input = userinput.replace('evaluate ', '')
        
    replacements = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',

        # addition
        'plus': '+',
        'added to': '+',

        # subtraction  
        'minus': '-',
        'subtracted from': '-',

        # multiplication
        'times': '*',
        'time': '*',
        'x': '*',
        'multiplied by': '*',
        'into': '*',

        # division
        'divided by': '/',
        'upon': '/',

        # addition
        ' raised to the power of ': '**',
        ' raise to the power of ': '**',
        ' raised to power of ': '**',
        ' raise to power of ': '**',
        ' raised to the power': "**",
        ' raise to the power': "**",
        ' raised to ': '**',
        ' raise to ': '**',
        ' raised to power ': '**',
        ' raise to power ': '**',
    }

    # Create a regular expression pattern that matches all the words that need to be replaced
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in replacements.keys()) + r')\b')

    # Use re.sub() to perform replacements in a single pass
    _input = pattern.sub(lambda match: replacements[match.group(0)], _input)

    return _input