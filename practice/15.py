def number():

    numbers = [10, 25, 8, 45, 15]
    max_number = numbers[0]

    for integers in numbers:
        if integers > max_number:
            max_number = integers

    print(max_number)

number()