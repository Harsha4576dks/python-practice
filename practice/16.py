def vowels():

    name = input("Enter a name:")
    vowels = "aeiou"
    count = 0

    for ch in name:
        if ch in  vowels:
            count = count + 1

    print(count)

vowels()