# FUNCTION IN PYTHON
#function is reusable block of code- that will be executed only when its called
# we can return any data/ and also pass parameters

#1. CREATE A FUNCTION:  - using 'def' keyword

def function_name(): #function definition
    print("hello this is the function")

print("------------------------")
    
#2. CALLING THE FUNCTION:  -using the function name

function_name()

print("------------------------")
#3. ARGUMENT:(args-short form)  - passing the information to the function, we can pass en-number of argument separated by comma.

def sample(f_name):  #f_name is called parameter-variable inside the () at the function definition.
    print("the function name along with the argument is"+ f_name)
sample("ALEXA")  #alexa is called the argument- values set to the function when its called.

print("------------------------")
    ##      1.No. of argument-parameter==argument not less or more.
    
"""def example(name):
    print("name"+name)       -this line will throw error as your passing 2 argument to 1 parameter
example("bob",9)  """    


print("------------------------")
    ##      2.Arbitary argument[*args]-- this is used when u dont know the number of argument passed to the argument

def example(*items):
    print("the item 2 is "+items[2]) #eraser- as its in the index 2.
    
example("pencil","pen","eraser","scale")

print("------------------------")
    ##      3.Key for argument[kwargs]- in case of random assigning values to the argument--done using 'key=value' syntax.
    
def practice(child1,child2,child3):
    print("child1 is "+child1+"child2 is "+child2+"child3 is "+child3) #child1 is melvin child2 is kelvin child3 is calvin.
    
practice(child2="kelvin",child3="calvin",child1="melvin")  # we are radomly give values in the key= value format

print("------------------------")
    ##      4.Arbitarty argument[** kwargs]--if they might send multiple data to the argument- we use this.
            #"RECIEVE DICTORNARIES OF ARGUMENT"
    
def practice2(**child):
    print("the child2 is"+child["child2"])  # we are calling like in the given child give the value of the key child2.

practice2(child1="melvin",child2="kelvin") 

print("------------------------")
    ##      5.Postional-Only Argument--prevent kwargs, enforce to follow order of the parameter,prevent unwanted chances
            #by users  -- use "/" keyword
            
def postional(child1,child2,/):
    print("this is child1"+child1+"child2 is"+child2)

postional("kelvin","calvin")  #this is child1 kelvin child2 is calvin
#if you use positional(child2="calvin",child1="kelvin") or positional(child1="kelvin",child2="calvin") - throw "ERROR"

print("------------------------")
    ##      6.Keyword-Only Argument-- used when the no. of the argument can be varing, it will execute without error or
            #break,let user to give the value- making it self explanatory. -- use "*" keyword
            
def key(*,kwarg_child1,kwarg_child2):   #for '*' we need to specify in the first itself. but for '/' we need to specify last.
    print("this is child1"+kwarg_child1+"child2 is"+kwarg_child2)
    
key(kwarg_child2="calvin",kwarg_child1="kelvin")  #this is kelvin child2 is calvin
# the name in the parameter and the argument should be matching else it will throw error for keyword only argument.


print("------------------------")
    ##      COMBINING (POSITIONAL+KEYWORD) ONLY ARGUMENT:

def combine(n1,n2,/,*,kwarg_n3,kwarg_n4):
    print(n1+n2+kwarg_n3+kwarg_n4)  #10 as its 1+2+3+4+5=10
    
combine(1,2,kwarg_n3=3,kwarg_n4=4) 

print("------------------------")
# 4. DEFAULT PARAMETER VALUE: if u define a value in the fun. definition that will be the default value.

def practice3(child="alice"):
    print("child name is "+child)

practice3("kelvin") # child name is kelvin
practice3("melvin")  #child name is melvin
practice3()  #child name is alice - as we have not passed any argument it will take the value in the parameter

print("------------------------")
# 5. PASS AN LIST OF ARGUMENT{ IT CAN BE OF ANY DATATYPE- STRING, LIST,DICTORNARY,SET,INTEGER AND ETC..}

def practice4(childrens):
    for c in childrens:
        print("child is "+c)

child=["melvin","kelvin","calvin"]       
practice4(child)

print("------------------------")
# 6. TO RETURN VALUE IN FUNCTION: {USE 'RETURN' KEYWORD}

def display(x):
    return x  # u cannot print as it will throw error like "you cannot concatinate int "

print(display(3))

print("------------------------")
#7. USING PASS STATMENT: {if u want to write the function code in future then use "pass" keyword to overcome the error
# -of the empty code----NOP[No operation happening]}

def pass_statement():
    pass

print("------------------------")
#8. RECURSION-- function call itself-provide more elegant/easy to understand

def factorial(x):
    if (x==1):
        return 1
    else:
        return (x*factorial(x-1))

y=factorial(3)
print(y)   # 6 as its 1*2*3=6


