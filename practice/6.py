def cars():
    cars = {
        "bmw": 20000000,
        "audi": 10000000,
        "benz": 15000000,
        "fortuner": 5000000,
    }

    expensive_car = ""
    cost = 0

    for name, price in cars.items():
        if price > cost:
            expensive_car = name
            cost = price

    print(f"The most expensive car is {expensive_car} with a price of {cost}.")

cars()
