def Integer():
    
    Number = int(input("enter a number:"))

    if isinstance(Number, int):
            print("number is an integer")
    else:
            print("number is not an integer")

Integer()