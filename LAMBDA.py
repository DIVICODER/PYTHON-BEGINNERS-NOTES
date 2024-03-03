        #LAMBDA IN PYTHON--- Is an anonymous function[unknown feature in fuction]
#1. Purpose of lambda over def[general function]--lambda provide a brief function within a short one line
    # which mean they provide more readablity 
    
#2. A lambda can have multiple aurguments for a single expresion example
add=lambda a,b:a+b
print(add(2,3))

#3. Using the function u can double, triple the number u sent to it

'''now we are explaining the execution of the below code
1. first we pass the 2 to the function[func()] mean that lambda a:a*2 will be returning to the mydouble
2. now we are trying to print mydouble(10) which mean 'a' will be 10 that results in  mydouble having 10*2 
3. resulting the output as 10*2=20'''
def func(n):
    return lambda a:a*n
mydouble=func(2)    # if you want the triple of a value then u give 3 here.
print(mydouble(10)) 

#they are mainly used in functional paradigm--functional paradigm means that focusus of functions that has multiple 
    #functions assigned as parameters and they work with it-- which can be achieved using lambda function

#map()[mapping an elements from an list to a variable] -- we use lambda function to it
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
values=list(map(lambda x:x+10,numbers)) #x will be values in numbers and they perform maping and operations and stored
    # stored in values as list -- performed type casting
print(values)   #[11, 12, 13, 14, 15, 16, 17, 18, 19] 

#filter()[we can filter elements based on conditions]-- we use lambda function to it
store=list(filter(lambda x:x%2!=0,numbers)) # we list only the elements in the list that follows this condition
print(store)    #[1, 3, 5, 7, 9]

#sorted()[we can sort the elements and store it in a list]-- we use lambda function to it
sort_num=sorted(numbers, key=lambda x:len(str(x)), reverse=True)
print(sort_num)
    #[1, 2, 3, 4, 5, 6, 7, 8, 9] this is the output it havent reverse as all the are singlular digits


# sort = sorted(numbers, key=lambda x: len(str(x)), reverse=False)
# print(sort)
fruits=["apple","orange","banana"]
print(sorted(fruits, key=lambda x: len(x), reverse=True))
    #['orange', 'banana', 'apple'] it is reversed here we just give len(x) because we are working with strings

number = [123, 45, 6789, 12, 9]
sorted_numbers = sorted(number, key=lambda x: len(str(x)), reverse=True)
print(sorted_numbers)
    #[6789, 123, 45, 12, 9] as they have a different number of digit counts like 2,3,4 digits so it is reversed accordingly.
    




