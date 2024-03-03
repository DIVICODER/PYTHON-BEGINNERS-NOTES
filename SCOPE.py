    #IN THIS WE WILL SEE WHAT IS SCOPE BASICS
    # A SCOPE MEAN THE AVAILABLITY OF THE VARIBALE ONLY WITHIN A REGION WHERE IT IS CREATED
    
####______NAME VARIABLE:-

'''Python will treat them as two separate variables, one available in the global scope
(outside the function) and one available in the local scope (inside the function)'''
z=123
def funct():
    z=321
    print("printing z value within the function block:",z)
print("printing z value outside the function block:",z)
print("\n")
funct()
print("\n------------")
#1. GLOBAL SCOPE--VARIABLE:
    #THE GLOBAL VARIABLE IS BE RETAINED IN THE MEMORY AS LONG AS THE PROGRAM RUNS.
    #THE VALUES IS PERSIST THROUGHOUT THE ENTIRE PROGRAM-- STAY TILL THE PROGRAM END
    #THEY ARE DECLARED OUTSIDE THE BLOCKS 
    #THEY CAN BE ACCESSED BY ANY BLOCKS TOO.
x=100
def func():
    print("within the function:",x)

print("outside the function:",x)
func()
print("\n")
    # IF YOU WANT TO MODIFY A GLOBAL VARIABLE 
def func2():
    global x
    x=90
    print("global x is modified to 90 within the function:",x)  #90

print("global x before the function call[in which they have modified the global x value=90]:",x)  #100
func2()
print("display the x value after the function call:",x)
    #because first the x is 100 globaly and you print the first statement outside the function, then you call function
    #where the global value of x is modified to 90 now and inside the function it will be 90 x got updated.
    
print("\n-----------------")
#2. LOCAL SCOPE --VARIABLE:
    #THE VALUE WONT BE RETAINED IN THE MEMORY FOR LONG RUN.
    #THE LIFE TIME OF THE VARIABLE IS TIED TO THE BLOCK-- IF FUNCTION EXITED THEN THEY WILL BECOME A GARBAGE VALUE.
    #THEY CAN BE ACCESSED ONLY WITHIN THE BLOCK ONLY.
    
def func3():
    y=10
    print("local scope value:",y)
func3()

# print("local scope value outside the function",y) #throw error as the y is unknown for others as its within the block

#NESTED FUNCTION USING LOCAL VARIABLE:
print("\n")
def func4():
    y=20
    def func5():
        print("printing local value from nested function is:",y)
    func5()
func4()




