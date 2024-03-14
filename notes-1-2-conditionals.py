# Conditionals
# Author: Tim Zou
# 15 February 2024

x=1_000_000
y=1

# if x > then y say so
# if is greater, say. IF is equal, say

if x<y:
    print("x is less than y")
if x>y:
    print("x is larger than y")
if x==y:
    print("x is equal to y")


if x<y:
    print("x is smaller than y")
elif x>y:
    print("x is larger than y")
elif x==y:
    print("x is equal to y")


if x<y:
    print("x is smaller than y")
elif x>y:
    print("x is larger than y")
else:
    print("x is equal to y")

# below are linking
#comment highlighted text by using ctrl+/

foo=input("enter number")#string

if int(foo)<-1 or int(foo)==0:
    print("foo is less than 1")
    print("or foo is equal to zero")
# can also use int function on input to make it easier
    

#check if foo is inside a range
# greater than one and less 1000
# on both side must have full statements
if foo>1 and foo<1000:
    print("foo is in the range of 2-999")
else:
    print("foo is outside the range of 2-999")

# 'or' is to see if either side is true
# 'and' is to see if both side is true