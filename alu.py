def add(a,b):
   return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
   c=0
   try:
      c=a/b
   except:
        c="Error"
   return c    
   
def mod(a,b):
   return a%b
