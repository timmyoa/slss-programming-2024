#loops and iteraitry
#author:Tim zou
#april 5 2024

#print something 10 times
for i in range(10):
    print("something")

#create a grocery list
# do something for each item in the list

grocery_list =[
    'blueberry muffins',
    'potato chips',
    'aluminium foil',
    'orange juice',
    'rtx 4070 super',
    'cereal'
]

for item in grocery_list:
    print(f"* {item}")
#skips when  get to rtx
    if item.lower()== "rtx 4070 super":
        print("NO RTX 4070 SUPER!!")
        break

# counting using a for loop

for i in range (100):
    print(i)

def py(num):
    for i in range(num):
        print("*"*i)

asd=input("num?")
asd=int(asd)
py(asd)