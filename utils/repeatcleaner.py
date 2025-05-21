import re

REPEATER = re.compile(r"(.+?)\1+$")

def repeated(s):
    match = REPEATER.match(s)
    return match.group(1) if match else None

def clean_repeat(query):
    if repeated(''.join(query.split(" "))) == None: 
        # no repeats. return the original query
        return query
    else:
        fundamental_period = repeated(''.join(query.split(" ")))

        split_fundamental_period = [*fundamental_period]
        split_query = [*query]
        i = 0

        final_string = ""

        for item in split_fundamental_period:
            if item == split_query[i]:
                final_string = final_string + item
            else:
                final_string = final_string + ' '
                final_string = final_string + item
                i = i + 1
            i = i + 1
        return final_string