import random
import datetime
# def is_in(string, list_of_inputs):
#     output = set(list_of_inputs).intersection(set(string.split(" ")))

#     if len(output) < 0:
#         # try another method
#         # TODO: FIX THIS
#         parent = list_of_inputs.join("").split(" ").join("") 
#         child = string.split(" ").join("")
#         if child in parent:
#             return True
#         else:
#             return False

def is_in(string, list_of_inputs):
    for input in list_of_inputs:
        if string in input:
            return True
    return False

def try_to_converse(string):
    if is_in(string, ['how are you', 'how are you doing', 'how are you today']):
        responses = ["Hi! I'm doing great, thank you for asking!", "I'm doing fine, thanks for asking!", "I'm doing good, thank you for asking!", 
                     "I'm doing well, thanks for asking!", "Being a machine, I'm always doing great!", "Hi! I'm doing great, thanks for asking! How about you?",
                     "Doing quite fine, thanks for asking!", "I'm doing wonderful. thanks for asking!"
                     ]
        return random.choice(responses)

    if is_in(string, ['hi', 'hello', 'hey', 'howdy']):
        responses = ['Hi there!', 'Hello!', 'Hey!', 'Howdy!', 'Greetings!', "What's up?", "Hi, How may i help you today?",
                     'Hello there!', # general kenobi :)
                     "Hi, I'm Nexus, your personal assistant. How may i help you today?", "Hi there, What would you like me to do today?",
                     "Hello! I'm Nexus. Let me know what you'd like to get done today!"
                     ] 
        return random.choice(responses)
    
    if is_in(string, ['good morning', 'good afternoon', 'good evening', 'good night', 'good day']):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 4: return f"Good Morning, shouldn't you be sleeping now? It's {hour} in the morning! I suggest going to bed early to wake up fresh the next day."
        elif hour >= 4 and hour < 12: return "Good Morning! I Hope you have a fantastic day ahead!"
        elif hour >= 12 and hour < 16: return "Good Afternoon!"
        elif hour >= 16 and hour < 21: return "Good Evening!"
        else: return "Good Night! Make sure you go to bed on time!"

    if is_in(string, ['thank you', 'thanks', 'thank you so much', 'thanks a lot']):
        responses = ["You're welcome!", "No problem!", "Anytime!", "Glad to help!", "You're welcome!"]
        return random.choice(responses)
    
    if is_in(string, ['bye', 'goodbye', 'see you later', 'see you soon']):
        responses = ["Goodbye!", "See you later!", "Take care!", "Bye!", "Goodbye!"]
        return random.choice(responses)
    
    if is_in(string, ['who are you', 'hu r u', 'who r u', 'what are you', 'what r u', 'what is your name']):
        responses = ["I'm Nexus, your personal assistant!", 
                     "I'm Nexus, your personal assistant. How may I help you today?", 
                     "I'm Nexus, your personal assistant. How may I assist you today?"]
        return random.choice(responses)
    
    if is_in(string, ['what can you do', 'what do you do', 'what are your capabilities']):
        responses = ["I can do a lot of things! I can help you with maths, units, timetables, and much more!"]
        return random.choice(responses)

    if is_in(string, ['what time is it', 'what is the time', 'time right now']):
        return f"The time is {datetime.datetime.now().strftime('%I:%M %p')}"

    if is_in(string, ['what day is it', 'what is the date', 'what is the day']):
        return f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}"

 
    else: return "error_unable_to_converse"