def vowels():

    word = input("Enter a word:")
    vowel_letters = "aeiou"
    count = 0

    for letter in word.lower():
        if letter in vowel_letters:
            count += 1

    if count:
        print(f"The number of vowels is {count}")
    else:
        print("No vowels")

vowels()