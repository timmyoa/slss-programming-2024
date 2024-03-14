#methods(string)
#Author: Tim
#feb-22-2024


#ask user what is the user
# if reply rainy then we tell them bring umbrella

weather= input("what is the weather?: ")
if weather=="rainy":
    print("you need umbrella!")
else:
    print(f"sorry, I don't understand {weather}")

#methods are function that works on object
    
if weather.lower().strip("!")=="rainy":
    print("you need umbrella!")
else:
    print(f"sorry, I don't understand {weather}")

print(weather.strip("r,a"))

#strip() gets rid of characters