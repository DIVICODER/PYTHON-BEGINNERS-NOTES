##      DICTIONARY  -- it can store any datatypes
#1. Store data in - "key:value" pair  ---- written in {}

thisdictionary={"name1":"calvin","age":34,"job":"software designer"}
print(thisdictionary)

#2. ORDERED AND CHANGABLE-- python 3.7 version  its ordered --- python 3.6 version its unordered
#3. DONT ALLOW DUPLICATES

thisDuplicate={"name1":"kelvin","job":"service sector","job":"full stack development"}
print(thisDuplicate) # name:"kelvin",job"full stack development" - as there will be overwritten.

#4. DICTIONARY LENGTH -- use len() function
print("the length of the this dictonary the orginal"+len(thisdictionary))

#5. ITEMS DATATYPES IN DICTIONARY:
Items={"integer":39,"strings":"helloword","boolean":False,"Color_array":["red","blue","green"]}
print(Items)

#6. TYPE()- keyword is used to get the datatype "dict" --dictionaries are defined as objects with the data type 'dict'
print("the datatype of the Items"+type(Items))  #<class 'dict'>

#7. DICTIONARY CONSTRUCTOR : [dict()-constructor]
thisDict=dict(name="kelvin",age=29,job="marketing")
print(thisDict)   #{name:kelvin,age:29,job:marketing}

#9. ACCESSING ITEMS: mainly we access to the values with the help of the key

thisdictionary={"name1":"calvin","age":34,"job":"software designer"}
print("orginal age"+thisdictionary["age"])
## accessing the value - done using get "values function" 

print("the accessing the value using  the function"+Items.values())

## accessing the key - done using get "key function"

print("we are accessing the key using the function"+Items.key())

## accessing the items syntax "dictinionary_name.items()"

print("we are now accessing the items in the items dictionary"+Items.items())

#10. CHECKING WHETHER THE KEY EXIST: using the "in keyword"

print("we are not checking that thisdictionary has age column")
if "age" in thisdictionary:
    print("present in it")
    
#11. CHANGING AND UPDATION OF THE DICTIONARY:-- change mainly happen only with the  help of the key 

# WE CAN USE THIS SAME METHOD TO ADD AN ITEM IN THE DICTIONARY
thisdictionary["age"]=20
print(thisdictionary)

print("-------------------------")
## Using update() function.
thisdictionary.upadate({"age":100})
print(thisdictionary)

print("-------------------------")

# WE CAN USE THIS SAME METHOD TO ADD AN ITEM IN THE DICTIONARY
thisdictionary["color"]="brown"
print(thisdictionary)
 
print("-------------------------")

#12. REMVOVING OPERATION- 
#Using pop(key) function

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

print("-------------------------")
#Using popitem() function-- pops the last key along with the values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) ##  {"brand": "Ford","model": "Mustang"}

print("-------------------------")
# Using the del dictionaryname[key] will delete that particular key-- key u del dictionaryname then the entire dictionary
#   will be deleted and if u try to print u will get the error.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) #  {"brand": "Ford"}

print("-------------------------")

#Using dictionaryname.clear() fuction is used - to clear the entire dictionary 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)  #{}

print("-------------------------")

#13. LOOPING THE DICTIONARY- FOR ITEMS/KEYS/VALUES TO BE PRINTED
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in this_dict.items():
  print(x, y)  #brand Ford model Mustang year 1964
  
print("-------------------------")
for x in this_dict.keys():
  print(x)  #brand model year
  
print("-------------------------") 
for x in this_dict.values():
  print(x)  #Ford Mustang 1964
  
print("-------------------------") 
#14. COPING DICTIONARY-- we cannot use dic1=dic2 as change in dic2  will affect the dic1[as dic1 will have the refrence of
# dic2] 

    #Using copy() build in function
dic2=this_dict.copy()
print(dic2)
print("-------------------------")

    #Using dict() build in function
dic3=dict(this_dict)
print(dic3)
print("-------------------------")

#15. NESTED DICTIONARY-- one dictinary inside the other
    #One way is -- creating separate dictinaries and then bringing it side a single dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
        # TO ACCESS TO THE ITEM IN A NESTED DICTIONARY WE USE DICTIONARYNAME[KEYNAME][NESTED KEYNAME_WITHIN_IT]
print(myfamily["child2"]["name"]) # child2 is nested dictionary that has name key within it
    
    #Second way is -- creating a single dictionary that have multiple dictionaries within it
    
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(my_family["child2"]["name"])




