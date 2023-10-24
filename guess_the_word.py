import random

name = str(input("Enter your name: "))
print("Good luck", name, "!")
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("\nGuess the alphabets")
guesses = ""
turns=12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("\nYou win")
        print("The word was:",word)
        break
    print()
    guess = str(input("\nGuess an alphabet: "))
    guesses += guess

    if guess not in word:
        turns -= 1
        print("\twrong")
        print("\tYou've",turns,"more guesses\n")
        if turns == 0:
            print("You loose")
