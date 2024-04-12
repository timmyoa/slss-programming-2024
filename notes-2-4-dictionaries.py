#notes - dictionarties

#big ideas:
#-a dictionary is a data structure
#-dictionaries map keys to value
#to use dictionaries use {}

person=[
    "john",
    "23 year old",
    "114514"
]
#get and print the person's name(?)
#use the index
print(person[0])
print(person[-1])#start from the last
# if calls a false index, code will break

#rewriting above as dictionary
person_dict={
    "name": "john",
    "age":"23 year old",
    "cc num": "4500 1023 2222 1111",
    "SIN num": "745 231 241",
    "roblox name":"ultimatecool_phantomshadowcontroller"
    }

#grabs value by key
print(person_dict["name"])

person_one={
    "name": "jim",
    "age":"42 year old",
    "cc num": "1145 1415 4111"
    }

#prints out everything
for info in person:
    print(info)
for key,value in person_dict.items():
    print(key,value)