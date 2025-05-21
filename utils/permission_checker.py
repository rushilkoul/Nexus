'''
    --------NEXUS PERMISSIONS--------
    Nexus has 3 permission levels:
        0. Restricted
        1. Standard
        2. Superuser
    
    - Superuser has all permissions, and can alter sensitive data
    - Standard has all permissions except altering sensitive data
    - Restricted will prevent users from running certain commands. will vary

''' 

import json 
_data = json.load(open("utils/data/data.json"))

permLevel = _data["localVars"]["user_level"]

def get_user_level():
    return permLevel

def check_permission(_permlevel):
    if permLevel >= _permlevel:
        return True
    else: return "Access Denied."