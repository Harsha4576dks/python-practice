def counter():

    word = input("Type a word , lets check if this is a palindrome:")
    reversed_word = ""

    for letter in word:
        reversed_word = letter + reversed_word

    if word == reversed_word:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

counter()