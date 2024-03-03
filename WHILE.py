# WHILE LOOP-- if you're not sure of the range, you could use this.

# using break in loop
i = 1
while i < 6:
    print(i, end=" ")  # end=" " is used to print statements within a single line.

    if i == 3:
        break   # used to break the loop
    i += 1    # we need to increment the i value, else it will fall into an infinite loop.
print("\n-------------------")

#using continue in loop
i = 1
while i < 6:
    print(i, end=" ")

    if i == 3:
        i += 1  # this increament is done to prevent i stuck with 3 leads to infinite loop
        continue   # used to continue the loop by skipping the rest of the code inside the loop
    i += 1
print("\n--------------")

#using pass -- where u can add ur futher code 
i=0
while i<4:
    if i==1:
        pass    # pass wont affect the code 
    i +=1
    print(i)

print("\n--------------")
# we can have an else for a while loop. If the while condition fails, then the else will be executed.
i = 0
while i == 0:
    print("o")
    i = 1
else:
    print("i")
print("-----------------")

