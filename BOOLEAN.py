        #BOOLEANS IN PYTHON
        
# represent--- 2 values-- True/False
#we need to check the condition and it will return whether the condition is true/false.

print(10<9)
print(10>9)
print(10==9)

# here we are checking the condition and if its true then the "if" statement is executed.
a=100
b=20
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
    
# having are usign "bool()" function

print("----------------------------------------------")
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

print(bool())   # here we dont have any string in it-- thats why its false.
print(bool("string"))   #here we have a string that why -- the output is true.

print("----------------------")
print(bool(0))  #here we have 0 as the input mean -- its false for number.
print(bool(30)) #here we have other number than 0 -- thats why its output is true.

print("----------------------")
print(bool([]))     #here we have no items in the list -- that why the output is false.
print(bool(["apple","orange","banana"]))    #here we have some items in the list that why--the output is true.

print("----------------------")
#we can even try this way--
x="hello_this is string"
print(x)

print("----------------------")
print("all the bellow condition led to false outputs..")
print("the {} is empty so the output is false:")
bool({})
print("the () is empty so the output is false:")
bool(())
print("the 'False' is given inside the function so the output is false:")
bool(False)
print("the 'None' is given inside the function so the output is false:")
bool(None)

print("------------------------")

#function return boolean[True/False]:
print("we are trying to to print the boolean of the class len function that actually return 0.")
class myclass():
  def __len__(self):
    return 0    #this function will always return 0 whenever the function is called

myobj = myclass()
print(bool(myobj))  #we are trying to print boolean of the function-- as it return 0-- the output will be false.

print("-------------------------")

print("we are trying to print the function that return false")
class myclass():
    def myfunc():
        return False    #this function will always return false so the output will be-- false.
print(myclass.myfunc())

print("----------------------")

print("we are trying to print the function that return true")
class myclass2():
    def myfunc2():
        return True #this function will always return true so the output will be true.
print(myclass2.myfunc2())   #we have said to print in myclass2 that have myfunct2 return statement to be printed..

print("-----------------------")
#   we are trying to print the boolean output using the another build in function called--"isinstance()"

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Creating instances
dog_instance = Dog()
cat_instance = Cat()
animal_instance = Animal()

# Using isinstance() for type checking
print(isinstance(dog_instance, Dog))      # True
print(isinstance(cat_instance, Cat))      # True
print(isinstance(animal_instance, Animal)) # True

# Checking against multiple classes
print(isinstance(dog_instance, (Dog, Cat)))       # True
print(isinstance(cat_instance, (Dog, Cat)))       # True
print(isinstance(animal_instance, (Dog, Cat)))    # False

