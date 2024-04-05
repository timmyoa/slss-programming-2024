#more functions
#Author: Tim Zou
# 4 april 2024

# U= untracked || 
# save process: save-> commit-> push 
# (save, commit is in here. push is in github)

#Multiply strings
greeting="hello"
print(greeting*2)

print("The quick brown dog fox jumps over the lazy dog."*2)

def star(num):
    value=""
    #returns given number of *
    if num== 0:
        value=="nothing"
    elif num>=1:
        value="*"*num
    return value

print(star(100))