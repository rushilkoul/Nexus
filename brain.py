from utils.units import convert
from utils.maths import evaluate
from utils.conversation import try_to_converse
from utils.timetables import get_period
from utils.repeatcleaner import clean_repeat


def think(query):
    
    # process the query and generate a response.
    #### QUERY CLEANUP #####
    ### if the user says the same thing twice
    query = clean_repeat(query)


    ############################ BEHAVIOUR TREE ##################################
    # have to make an ML deep learning model for this :///
    if query == "stop":
        return ""
    if query == "reboot":
        return "COMMAND_REBOOT"
    if query == "terminate":
        return "COMMAND_REBOOT"

    # basic conversation skills
    conv = try_to_converse(query)
    if conv != "error_unable_to_converse":
        return conv

    # utilities (units, maths, etc)
    if "convert" in query:
        return convert(query)
    elif "period" in query:
        return get_period(query)
    
        # maths 
    elif "evaluate" in query:
        return evaluate(query)
    elif "what is" in query:
        return evaluate(query.replace("what is", "evaluate"))
    elif "calculate" in query:
        return evaluate(query.replace("calculate", "evaluate"))
    
    else:
        return "Sorry, I could not understand that."