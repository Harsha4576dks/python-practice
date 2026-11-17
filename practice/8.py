def counter():

    word = input("Type a word , lets check if this is a palindrome:")
    if word == word [::-1]:
        print("This is a palindrome")
    else:
        print("This is not a plaindrome")

counter()