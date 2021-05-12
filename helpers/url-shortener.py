import random  
import string  

def generator(): 
    
    alias = ''.join((random.choice(string.ascii_lowercase) for x in range(5)))
    print(alias)  
    return alias