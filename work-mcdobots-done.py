#conitions and string methids work exercise
#Author: Tim zou
#Feb-20th-2024

print("Do you want fires with your meal?")
a=input("Answer (yes/no): ").lower().strip("!,.?")
if a== "yes"or a=="yeah" or a =="sure" or a=="ok" or a=="okay":
    print("Enjoy your meal with fries!!")
elif a== "no" or a=="nope":
    print("Here is your meal without fries!")
else:
    print(f"I am sorry, but i do not understand '{a}'.")



#done