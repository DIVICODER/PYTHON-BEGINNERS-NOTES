        ## CLASS AND OBJECT IN PYTHON
  
#1. CLASS:-  a blueprint for creating a object that can have

class basic:
    x=10    #CLASS VARIABLES
    
    def __init__(self,n,a): #CONSTRUCTOR
        self.name=n     #self-- IS JUST A REFRENCE TO THE CURRRENT INSTANCE.
        self.age=a
        
    
    def __str__(self):      #SPECIAL METHOD/MAGIC METHOD-- CONTROL OF WHAT TO BE RETURNED AS STRING--CAN BE REPLACED 
        # USING PRINT(OBJECT_NAME.ATTRIBUTES)
        
        print("THIS IS INSIDE THE __STR__()")
        return f"the name is {self.name} and there age is {self.age}"
    
    
    def func(self):
        print("this is statement inside function!!")    #METHODS 
        
        
    def func2(param):
        print("the name is", param.name, "and there age is", param.age)    #METHOD THAT PRINTS THE ATTRIBUTES
        
        
b1=basic("alice",25) #OBJECT FOR CLASS IS CREATED--PASSING THE ARGUMENT TO THE CONSTRUCTOR

print("printing the x value before modifying:\n")
print(b1.x) #ACCESS TO VARIABLE IN CLASS USING OBJECT


print("\n")
b1.x=30     #MODIFY THE PROPERITES IN THE CLASS

print("printing the x value after the modifying:\n")
print(b1.x)


print("\n")
del b1.x    #DELETE OBJECT PROPERITES

print("we have deleted the x value")


print("\n")
b1.func()   #FUNCTION CALL USING OBJECT / OBJECT METHOD


print("\n")
b1.func2()  #FUCNTION CALL THAT PRINTS THE ATTRIBUTES OF THE CLASS USING OBJECT / OBJECT METHOD


print("\n")
print(str(b1))  #TRYING TO PRINT THE STATEMENT IN THE STR()FUNCTION.


print("\n")
print("we have now deleted the object b1 which we have created for the basic class")


#2. 'PASS' KEYWORD IN CLASS IF U WANT TO USE THE CLASS FOR THE FUTHER-- AND THEY SHOULDN'T THROW ERROR NOW
print("\n")
print("I have created a practice class which is having pass keyword in it")

class practice:
    pass

