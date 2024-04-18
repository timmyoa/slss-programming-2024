# classes and objects 

#big ideas :
# -classes allow us to couple data and functions together
# -object are the actual representives of the classes in our python scripits

#create a pokemon class; this repersnet a pokenon

class Pokemon: #use capital letter for class name(conventional)
    def __init__(self): 
        """ special method/ function called constuctor. contains all the properties/variable that describe a pokemon"""
        self.name = ""
        self.id= 0
        self.weight=0
        self.height=0
        self.type="normal"
        self.actual_cry="114514!!" #the defulte value

        print("a new pokemon is created")
    def cry(self):
        """this is the sound: pikapi
        returns the string of the sound"""
        return self.actual_cry
    def eat(self,food:str):
        "where to feed the pokemon, what it eats"
        if food.lower()=="berry":
            return f"{self.name} ate the berry"
        if food.lower()=="potion":
            return " it healed!"
        else:
            return f"smacks the {food} away"

class pikachu(Pokemon):
    def __init__(self,name="pickachu"):
        #call constructor of parent class
        super().__int__()
        #assign the defult value to properties
        self.name=name
        self.id=25
        self.type="Electic"
        self.cry="pikachu"
    def thunderbolt(self, defender: Pokemon):
        """attack another pokemon
            params:
            -defenders:defending pokemon
            returns:
            -str representing result of attack"""
        response=f"{self.name} used thundershock on {defender.name}"
        if defender.type.lower()in ["water","flying"]:
            response=response +"It was super effective"
#create two new pokemon using our class
# make one pokemon that is pikachu
# make one pokemon of choice
pokemon_one = Pokemon()

#chaning properties
print(pokemon_one.name)#gives nothing
pokemon_one.name="pikachu"
print(pokemon_one.name)
pokemon_one.id="123213123"
pokemon_one.type="eletric"

#using cry method
pokemon_one.actual_cry="11451514!!!!!!!!!!!!!"
print(pokemon_one.actual_cry())
print(pokemon_one.eat("berry"))

pikachu_one=pikachu()
pikachu_two=pikachu("speedy")

print(pikachu_one)
print(pikachu_two)

print(pikachu.thunderbolt(pokemon_one))
