# Local, Enclosing, Global, Built-in

x = 'global x'
#global because it is in main indent in the file
print(x)

def test():
    
    global x #this is to tell python to change the global var
    x = 'local x'
    y = 'local y'
    #this var is local in the test func
    print(y)
    print(x)

test()
print(x)