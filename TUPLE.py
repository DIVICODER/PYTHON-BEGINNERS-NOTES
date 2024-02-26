### TUPLE IN PYTHON

#1. Used to store multiple items in single variable-- they are separated by comma

tuple0=("madam",)   #tuple=("hi") it is invalid as there is no comma
tuple1=("hello","hi","hai")
print(tuple0)
print(tuple1)

print("------------------------")
#2. We can get the length of the tuple using len() function

print(len(tuple0))
print(len(tuple1))

print("------------------------")

#3. We can count the items in the tuple

tu=(1,2,2,3,4,3,4,5)
print(tu.count(3))  # 2- as the no. of 3 in tu is 2 times

print("------------------------")

#4. We also have type() function to get the tuple of the iterable- such as class 'tuple' / class 'list' and so on.

print(type(tuple0))

print("------------------------")

#5. We can get the index of the particular item in the tuple

print(tu.index(4))  # 4 as 4 is present in 4th index
print(tu.index(2))  # 1 as the 2 is present in 1st index while encounting from left ->right

print("------------------------")

#6.. It is unchangable, indexed, allow duplicates,ordered - while the 'set' is unchangable,no indexing, no duplicated
#unordered too.

#UNCHANGABLE/ IMMUTABLE: we cannot add or remove

#tuple1[0]="bye"
#print(tuple)  #it will throw error

#INDEXED: can use index to access

print(tuple1[2])

#ORDERED : the order is fixed and defined

for element in tuple1:
    print(element)   #hello  hi   hai
    
#ALLOW DUPLICATES: the set wont allow as it doesn't have indexing while the tuple has it 

tuple2=("apple","orange","mango","apple","orange")
print(tuple2)

print("------------------------")

#7. we can have convert any of the iterable[list,dictornarity,set] to tuple using "TUPLE CONSTRUCTOR-tuple()"

my_string="divya"
print(tuple(my_string))  # ('d','i','v','y','a')

print("------------------------")

#8. Tuple can store different type of data types too.

tuple3="hello","hi","bye","welcome"   #we can use () or without that also sometime it will work
tuple4=3,5,6
tuple5=("hello",[2,3,8],90,6.0,'j')
print(tuple3)
print(tuple4)
print(tuple5)

print("------------------------")

#9. Accessing : can be done using range, positive, negative

print(tuple2[1:3])   # ('orange', 'mango') - we dont include the 3 index we will display 1,2 indexed only
print(tuple3[-2])    # bye -  as "welcome" is -1 and "bye" is -2. when you start from left -> right start from -1 not 0.
print(tuple5[1])     # [2, 3, 8] as its from right -> left so indexing starts from 0.

print("------------------------")

#10. Check if item exist: use 'in' keyword

if "apple" in tuple2:
    print("yes its present")

print("------------------------")

#11. Add items in tuple- this can be done by converting it to list and perform operation, or combine two tuples

# COMBINE TWO TUPLES/ ADD TUPLE TO TUPLE:

print(tuple0+tuple1) #tuple0=("hello",) tuple1=("hello","hi","hai")

#COVERT TO LIST AND PERFORM APPEND OPERATION:

y=list(tuple4)
y.append(1)  
print(tuple(y))   # (3,5,6,1)

print("------------------------")

#12. remove an item in tuple by converting into list or we can completely delete the full tuple

#CONVERT TO LIST AND PERFORM REMOVE OPERATION:

x=list(tuple5)
x.remove('j')
print(tuple(x))  #('hello', [2, 3, 8], 90, 6.0)


print("------------------------")

#DELETE THE TUPLE ITSELF: using del() function

thistuple=("how","are","you")
del thistuple  # the tuple is deleted here
# print(thistuple)  #it will throw error as the tuple is deleted

print("------------------------")

#13. We can even multiple the tuples
sample=tuple5*2
print(sample)

print("------------------------")

#14. We can perform packing and unpacking in the tuple 

print("------------------------")

#PACKING: normally assigning values to the tuple

tuple6=("apple", "banana", "cherry","mango")
print(tuple6) # we are packing the values to the tuple6

print("------------------------")

#UNPACKING: we can extract the values back with the help of other variables

(red,blue,green,grey)=tuple6   #now the red,blue and green variable point to the item in the tuple6
print(red) #apple
print(blue) #banana
print(green) #cherry
print(grey) #mango

print("------------------------")

#USING ASTERISK (*): if the varible pointing to is <the variable in original

(red,*purple)=tuple6
print(red)  # apple
print(purple) #banana,cherry,mango- as we have not assigned 3rd varible this purple will hold the remaining

print("------------------------")

(red,*purple,orange)=tuple6
print(red)  #apple
print(purple)  #banana,cherry  - as it has * symbol it hold more than one while others can hold and point only one in it
print(orange) #mango

print("------------------------")

#15. We can loop the items in the tuple using while,for[using 'in' keyword/ index concept]

# tuple6=("apple", "banana", "cherry","mango")
#FOR LOOP:
for i in range (len(tuple6)):   #using indexing concept
    print(tuple6[i])

print("------------------------")

for element in tuple6:
    print(element)

print("------------------------")

#WHILE LOOP:
i=0
while i<len(tuple6):
    print(tuple6[i])
    i=i+1
