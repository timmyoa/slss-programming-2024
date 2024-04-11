#Bounus Large Coke
#Author: Tim Zou
#Date: April-11-2024

def calculate_for_3(num:int):
    #int to make it no decimal because there is no 0.3 large coke
    real=int(num/3)
    print(f"Calculations:  {num}/3={real}")
    return real
def calculate_for_2(num:int):
    real=int(num/2)
    print(f"Calculations:  {um}/2={real}")
    return real
print("Hello! Here at MC, every 3 boxes of fries, or 2 boxes of chicken wings, or 2 small apple pie gives you a free large coke! ")
asd=input("Would you like to buy any?(yes/no): ").lower().strip("!")
while asd not in [ "yes", "no"]:
    print("Please enter a vaild result.")
    asd=input("Would you like to buy any?(yes/no): ").lower().strip("!")
if asd=="no" :
    print("Ok, goodbye!")
elif asd== "yes":
    z=input("would you like to buy the chicken wings, fries, or small apple pies?: ").lower().strip("!",)
    while z!= "chicken wings" and z!="fries" and z!="small apple pies":
        print("please enter a vaild result.")
        z=input("would you like to buy the chicken wings, fries, or small apple pies?: ").lower().strip("!")
    x=int(input(f"How much {z} would you want?: "))
    if z=="fries":
        y=calculate_for_3(x)
    elif z=="chicken wings" or z=="small apple pies":
        y=calculate_for_2(x)
    print(f"Here is your {x} number of {z} and {y} number of large cokes!")
    print("Enjoy!!!!!!!!!!")

