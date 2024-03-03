    #WE WILL SEE OF HOW TO GET THE INPUT FOR THE USER
    # PYTHON WILL TAKE ALL INPUT AS A STRING ONLY
    
# WE CAN READ A INPUT FROM A TXT FILE ALSO

with open(r"C:\Users\LENOVO\anaconda3\PYTHON PRACTICE\input.txt", "r") as file:
    user_input = file.readline().strip()
    print("User Input:", repr(user_input))
    #repr() is used when you want a more detailed, programmatic representation of an object. 
    #often used for debugging or logging.

# WE WILL USE THE "input()" function-- TO GET THE INPUT FROM USER
x=input("enter the input:")
print(x)

#  WE CAN USE "getpass()"function -- THIS IS MAINLY USED TO GET PASSWORD FROM USER, AS U WONT ABLE TO SEE OF WHAT U ENTER

from getpass import getpass
y=getpass("enter the input:")
print(y)

# WE HAVE RAW_INPUT FUNCTION IN PYTHON 2 BUT THIS VERSION DOESN'T SUPPORTS IT

# GET WORDS FROM SENTENCE
output=input("enter the sentence i will give words of it:")
for i in output.split():     #we will use split to split the words
    print(i)
    
# GET NUMBER AND WORD SEPARATELY
num_word=input("enter the number and what words:")
num,word=num_word.split()
print(num)
print(word)

