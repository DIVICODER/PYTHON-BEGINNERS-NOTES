        #ARRAY IN PYTHON
        
#IN ARRAY WE MAINLY WORK WITH CHARACTERS AND NUMERICALS IF YOU WANT IT TO HOLD STRING THEN BETTER USE WITH THE HELP OF LIST.
#WE CAN ALSO PERFORM ARRAY WITH THE HELP OF LIST
#we have array module from where we need to import array
from array import array     # we are trying to import array from array module directly

#   CREATING
arr=array('i',[1,2,3,4,5,6,7,8,9,0,5,5])

#   ACCESS USING LOOP
for x in arr:
    print(x,end=" ")

print("\n-----------")
#   ACCESS USING INDEXING
print(arr[3])   # as the index start from 0 the 3 index we will have number 4

#   REMOVING ELEMENT USING VALUES
print("value 0 is removed")
arr.remove(0)
for x in arr:
    print(x,end=" ")

#   TO PRINT THINGS IN NEXT LINE
print("\n")

#   POP ELEMENT USING INDEX
print("the poped value is ",arr.pop(2))
for x in arr:
    print(x,end=" ")
    
#   COUNT ELEMENT
print("\n")
print("the number of 5 in the array is",arr.count(5))
print("\n-----------")

#   LENGTH OF ARRAY
print("the length of array is ",len(arr))

#   ADDING ELEMENTS IN ARRAY
print("we are  appending 100 to the array")
arr.append(100)
for x in arr:
    print(x,end=" ")
print("\n")

#   REVERSING AN ARRAY
arr.reverse()
print("this is the reversed array")
for x in arr:
    print(x,end=" ")
print("\n")

#   ADD AT PARTICULAR LOCATION
arr.insert(2,20)
for x in arr:
    print(x,end=" ")
print("\n")

#   COPYING THE ARRAY
dupl=arr.__copy__()
print("we are printing the duplicate of the array")
for x in dupl:
    print(x,end=" ")
print("\n")

#   CLEARING THE DUPLICATE ARRAY
print("clearing the duplicate array")
dupl=array('i')
for x in dupl:
    print(x,end=" ")
print("\n")

print("this is my orginal array")
for x in arr:
    print(x,end=" ")
print("\n")
