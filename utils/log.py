import time

def log(file, log, response):
        with open(f'./logs/{file}.txt', 'a') as f:
                f.write(f"\n{time.strftime('%a, %d %b %I:%M %p')} > {log}\n\tReponse: {response}")
                
def inf(file, log, response):
        with open(f'./logs/{file}.txt', 'a') as f:
                f.write(f"\n{time.strftime('%a, %d %b %I:%M %p')} > {log}\n\t {response}")