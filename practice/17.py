def even_numbers():

    numbers = [10, 15, 20, 30, 35, 40]
    even_list = []

    for ch in numbers:
        if ch % 2 == 0:
            even_list.append(ch)

    print(even_list)  

even_numbers()