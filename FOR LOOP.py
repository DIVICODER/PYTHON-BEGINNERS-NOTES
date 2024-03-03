# FOR LOOP-- if you know the no. of iteration count then u can go with for for loop.
fruit=["apple","orange","berry","passion"]
for x in fruit:
    print(x,end=" ")

print("\n---------------")

# we can use else for loop too
for x in fruit:
    if fruit=="banana":
        print("hello")
else:
    print("else condition")

print("\n----------------")

# we can use break in for loop
for x in fruit:
    print(x,end=" ")
    if x=="berry":
        break
print("\n----------------")

#we can use continue in for loop
for x in fruit:
    if x=="berry":
        continue
    print(x,end=" ") #on giving the print after this continue ensure a clear visibility of the functionality of the continue.
print("\n----------------")

#We can use pass in for loop
for x in fruit:
    print(x,end=" ")
    if x=="berry":
        pass    # pass keyword wont affect the code if ur use this then u can write any code in this place later.
print("\n----------------")

#we can use nested for loop
veg=["carrot","beans","onion","tomato"]
for x in fruit:
    for y in veg:
        print("\n---")
        print(x,y)
print("\n-----------------")

#we can use ranges in for loop
for x in range(4):
    print(x)    #0,1,2,3 we wont include the 4 
print("\n-----------------")

for x in range(3,4):
    print(x)    #3 because within 3,4 range we have only 3 because we cannot include 4
print("\n-----------------")

#we can even access to the characters in a string using for loop
for x in "banana":
    print(x)    # we access to the character of the banana and print separately.
    
#the else statement wont be executed if there is loop is terminated due to break keyword
for x in fruit:
    print(x)
    if x=="orange":
        break
else:   # this else wont be executed as in "if" statement we are saying to break the else will be executed if for condition
    #fails
    print("orange is not there")
print("the loop is over")
        
        
