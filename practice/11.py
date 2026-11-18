def prime():

    number = int(input("Enter a number:"))
    

    if number <= 1:
        print("not a prime number")
        return
    
    for i in range(2, number):
        if number % i == 0:
            print("not a prime number")
            return
        
    print("prime number")        

prime()