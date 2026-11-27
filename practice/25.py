def rag():

    text = input("Enter a sentence: ")
    words = text.split()

    for word in words:
        print(f"{word}: {len(word)}")

rag()