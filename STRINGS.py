
#1. STRING LITERAL IS THE SEQUENCE/INSTANCE OF CHARACTERS.
#2. A STRING IS A DATATYPE WHICH REPRESENT THE TEXTUAL DATA. THEY CAN BE CREATED USING STRING LITERALS.
#3. STRING IS AN ARRAY OF BYTES REPRESENTING THE UNICODE CHARACTER.
#4. WE DONT HAVE ANY CHARACTER IN PYTHON EVEN A CHARACTER IS CONSIDERED AS A STRING WITH LENGTH
#5. STRING CAN BE CREATED USING SINGLE/DOUBLE/TRIPLE QUOTES
#6. INDEX FROM BACK TO FRONT WILL BE -1 -> -value

#CREATING A STRING===

# Single quotes
single_quoted_string = 'Hello, World!'
print(single_quoted_string)

# Double quotes
double_quoted_string = "Python Programming"
print(double_quoted_string)

#multiline string 
a="""hello this is an multiline string with triple double quotes"""
print(a)
b='''hello this is an multiline string with triple single quotes'''
print(b)

#GETTING STRING LENGTH

a='hello'
print(len(a))       

#USING ESCAPE CHARACTER- there will be an issue while using '/ tabspace next line - cause an illegal declaration
a='I\'m meena'  #\ for ' insert
b='hi blankspace \\ this is me.' #\\ for \ insert
c='hello \bworld' #\b for earse one backspace
d='hello\tworld' # \t for tabspace
e='hello\nworld' #\n for nextline
print(a)
print(b)
print(c)
print(d)
print(e)


#CHECKING A CHARACTER IN THE STRING: using 'in' keyword=== TO CHECK NOT PRESENT: using 'not in' keyword

b="hello this is a free classes"
print("free"in b) #seeing that free is present in b string  array

b="hello this is a free classes"
print("present'"not in b) #we are checking a string isn't present in the string array

#STRING OPERATION==


## String cannot be concatenate with number
## but we can combine using format() method that number will be placed in the {} placeholder
#1. Concatenate:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

age=80
text="hello my age is {}"
print(text.format(age))

a=5
b=2
c=a+b
t="the a is {} and b is {} is {}"
print(t.format(a,b,c))

#you can even arrange the order in which it need to print
t="the a is {} and b is {} is {}"
print(t.format(a,b,c))



#2. Repetition:
greeting = "Hello "
repeat_greeting = greeting * 3
print(repeat_greeting)  # Output: Hello Hello Hello


#########=== STRING IS AN ARRAY:- that can be accessed using index of the array, the default first index is 0

#3. Accessing a Character: using index
message = "Python"
first_char = message[0]  # Indexing starts from 0
print(first_char)  # Output: P



#4. Slicing: extract substring
text = "Programming"
substring = text[0:4]  # Extract characters from index 0 to 3 (not including 4)
print(substring)  # Output: Prog

start_slice = text[:5]  # here were are starting from 0 index to 4 index(5 is not included)
print(start_slice) #Output: Progr

end_slice = text[5:9]  # here were are starting from 0 index to 4 index(5 is not included)
print(end_slice) #Output: Progr

negative_slice = text[-5:-2] #here if we start from left-> right move in negative indexing
print(negative_slice) # Output: mmin m->-5 n->-2



#5. Formatting String: f-strings is used- expressions
# inside curly braces {} are evaluated at runtime and their results are inserted into the string
name = "Bob"
age = 22
formatted_string = f"My name is {name} and I'm {age} years old."
print(formatted_string)
# Output: My name is Bob and I'm 22 years old.


#Older method for formating

name = "Alice"
age = 25
formatted_string = "My name is {} and I'm {} years old.".format(name, age)
print(formatted_string)
# Output: My name is Alice and I'm 25 years old.



#STRING METHODS: built in methods for string manipulation=====

text = "   Python Programming   "

# Removing whitespace
trimmed_text = text.strip()
print(trimmed_text)  # Output: Python Programming

# Converting to lowercase and uppercase
lowercase_text = text.lower()
uppercase_text = text.upper()
print(lowercase_text)  # Output:    python programming   
print(uppercase_text)  # Output:    PYTHON PROGRAMMING   

# Finding and replacing
index_of_p = text.find('P')
replaced_text = text.replace('Programming', 'Code')
print(index_of_p)  # Output: 3
print(replaced_text)  # Output:    Python Code

#Split string--The split() method returns a list where the text between the specified separator becomes the list items.
a="Hello,World"
print(a.split(",")) # returns ['Hello', ' World!']

#Count() is used to count the number of word
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)  #2- as the count of apple is 2 in the txt

#Finding a string- using find()
txt="hello this is me!"
y=txt.find("me")
print(y) # 14 as at 14th place the me is starting 

txt="hi this is me"
e=txt.find('i',3,8)  # text_name.find(string/character,starting index, ending index)
print(e) # 5 as the e found first in 3th position
