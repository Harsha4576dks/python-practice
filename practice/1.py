def numbers(): 
    numbers = [10, 15, 20, 25, 30, 35, 40]
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)


    print(even)
    return even

numbers()