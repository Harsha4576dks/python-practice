def Largest():
    numbers = [10, 45, 20, 35, 45, 30]
    largest = second_largest = float("-inf")

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif largest > number > second_largest:
            second_largest = number

    print(second_largest)

Largest()