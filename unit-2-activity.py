#bounus food
#Author: Tim Zou

def calculate_for_3(num:int):
    real=int(num/3)
    print(f"Calculations:  {num}/3={real}")
    return real
def calculate_for_2(num:int):
    real=int(num/3)
    print(f"Calculations:  {num}/3={real}")
    return real


print("Hello! Here at MC, every 3 boxes of fries, or 2 boxes of nuggets, or 2 small apple pie gives you a free large coke! ")
asd=input("Would you like to buy any?(yes/no): ").lower().strip("!")
while asd not in [ "yes", "no"]:
    print("Please enter a vaild result.")
    asd=input("Would you like to buy any?(yes/no): ").lower().strip("!")
if asd=="no" :
    print("Ok")
elif asd== "yes":
    z=input("would you like to buy the nuggets, fries, or small apple pies?: ").lower().strip("!",)
    while z!= "nuggets" and z!="fries" and z!="small apple pies":
        print("please enter a vaild result.")
        z=input("would you like to buy the nuggets, fries, or small apple pies?: ").lower().strip("!")
    x=int(input(f"How much {z} would you want?: "))
    if z=="nuggets":
        y=calculate_for_3(x)
    elif z=="fries" or z=="small apple pies":
        y=calculate_for_2(x)
    print(f"Here is your {x} number of {z} and {y} number of large cokes!")

