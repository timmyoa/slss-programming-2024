#function replacer
#name: Tim zou
#date: feb 27 2024

def main():
    x= input("Enter a sentence with noodles and 100: ")
    return x

def translate(x):
    x=x.replace("100","💯").replace("noodles","🍜").replace("Noodeles","🍜").replace("noodle","🍜").replace("Noodle","🍜")
    print(x)


translate(main())



#checked (no need to hand in)