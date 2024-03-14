#random function
#Author: Tim Zou
#Mar-11-2024
import random

#slot machine and rolls used

slot1=slot2= slot3=0
rolls=0
while slot1 != 7 or slot2 != 7 or slot3 != 7:
    rolls+=1
    slot1=random.randrange(1,12)
    slot2=random.randrange(1,12)
    slot3=random.randrange(1,12)
    print(f"result:  {slot1} | {slot2} | {slot3}")
   
print(f"Rolls: {rolls}")
if rolls<=10:
    print("Woah! Lucky")
print("If one roll costs $2 and winning gives $1000")
money=1000-rolls*2
if money<=0:
    print(f"You have lost: {money}")
elif money>=0:
    print(f"You have gained: {money}")
print(f"Casino gains {money*-1}")