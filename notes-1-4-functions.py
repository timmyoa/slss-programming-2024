#Functions
#feb-26-2024

#print() input() are functions

#function: block of reuseable code with a name

#how to make function:
# def <function_name>():
#   <block>
# convention: only use lowercase and underscore (for space)
#the code has to be indented

def say_hello():
    print("Hello!")

#nothing happen if the functions is used
#below is how it is ran:
say_hello()
say_hello()

#parameter () is the input of the function
#like print("jimmy")<--this is the input

#creating a function called say_hello _params
#print f"hello {parameters}"

def say_hello_params(name): #<-- the input
    print(f"Hello {name}!")

#now can enter input on code page to get thing on 
    
say_hello_params("jim")

#return key word:
# create a function called how_big:
#takes a number as a imput
# it returns how big the number is

def how_big(num):
    if num<0:
        return "very small"
    if num<10:
        return "pretty small"
    if num<100:
        return "small"
    if num<1000:
        return "pretty big"
    return "very big"

print(how_big(1))

result = how_big(1_000_000)
print(result)

#create a function called adder
#accept 2 numbers
#then return the sum of both numbers

def adder(x: int,y: int):
    return x+y

result=adder(1,1)
print(result)