# mark into percentage program
# Name: Tim Zou
# Mar-4-2024

# ask for multiple class's test's mark and total mark, and give reply to total marks


def percentagereply(z):
    if z>=0.85:
        return f"{name}, good job!"
    elif z>= 0.6:
        return f"{name}, that is pretty good!"
    else:
        return f"{name}, you can do it!"

print("Hello user!")
name=input("What is your name!: ")
x="yes"
total=0
runtime=0

while x.lower()!="no":
    cl=input("what class do you have?: ")
    a1=int(input(f"{name}, what mark did you get?: "))
    a2=int(input(f"{name}, what is the total mark?: "))
    print(f"{name}, your precentage for {cl} is {int(a1/a2*100)}%!")
    runtime=runtime+1
    print(f"Amount of classes are {runtime}!")
    x=input("do you have another class?: ")
    total=total+a1/a2*100
print(f"your average is {int(total/runtime)}%!")
print(percentagereply(total/runtime/100))
print("Bye!")
#done