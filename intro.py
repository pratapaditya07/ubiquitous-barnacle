###chalo shuru karte hai
##
message= "hello world"
print(message)
##
##
message= 'hello\' world'
print(message)
####basically jab hum \ lagate hai to uske baad jo bhi hota hai uski value khatam ho jaati hai
####JESE UPAR HUI HAI
##
message= "hello' world"
print(message)
####YA FIR SINGLE QUOTES KE BADLE DOUBLE QUOTES LAGA LO
##
message= '''hello\' world'''
print(message)
####YA AISE TRIPPLE SINGLE QUOTES LAGA SAKTE HAI
##
####HOW TO FIND THE NUMBER OF CHARACTERS IN A STRING
message = "i am reading a book called Atomic Habit written by JAMES CLEAR"
print(message)
print(len(message))
####we use len(length) function to find the number of characters
##
####how to find what's written in index
message = "i am reading a book called Atomic Habit written by JAMES CLEAR"
print(message[0])
#### WE USE "[]"(SQUARE BRACKET)
##
####what if we want to write whole string in upper /lower case
message = "i am reading a book called Atomic Habit written by JAMES CLEAR"
print(message)
print(message.upper())
print(message.lower())
##
####COUNT COMMAND
message = "i am reading a book called Atomic Habit written by JAMES CLEAR"
print(message.count("a"))
##CASE SENSITIVE!!!!!
##
####FIND COMMAND
message = "i am reading a book called Atomic Habit written by JAMES CLEAR"
print(message.find("called"))
####FIND COMMAND WILL TELL U THE INDEX NUMBER OF THAT ELEMENT THAT U ASKED FROM THE STRING
####IF IT CANT FIND THAT PARTICULAR WORD IT WILL GIVE -1 AS THE OUTPUT
##
##
####REPLACE FUNCTION
message = "i am reading a book called Atomic Habit written by JAMES CLEAR"
message = message.replace("Atomic Habit", "Human Psychology")
print(message)
print(message.upper())
print(message.lower())


##ADDITION OF TWO STRINGS
message = "hey i want to tell u something,"
greeting = "It really accentuates your face."
my_message = message + " " + greeting
print(my_message)

##ANOTHER WAY 2:
my_message='{} {}'.format(message,greeting)
print(my_message)

##ANOTHER WAY 3:
my_message = f"{message} {greeting}"
print(my_message) 

print(dir
      (message))















