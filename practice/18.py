def duplicate():

    numbers = [10, 15, 25, 25, 34, 34, 55]
    real_list =  []

    for num in numbers:
        if num not in real_list:
            real_list.append(num)

    print(real_list)

duplicate()