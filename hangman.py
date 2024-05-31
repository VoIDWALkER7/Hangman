import random
print("Hello, Welcome to My Version Of HangMAN")
print("---------------------------HANGMAN  (VOID's VERSION)------------------------------------")
words=["peresphone","hades","cereberus","zeus","hercules","aeris","hell","olympus"]
secret_word=random.choice(words)
display_word=[]
for i in secret_word:
    display_word.append("_")

print("\t\t\t ",display_word)

    #guess = input("Enter a letter").lower()
chances = len(secret_word) + 5
print(f"You have {chances} guesses. Everytime you get wrong, you lose one guess")
game_over = False
while not game_over:
    guess = input("Enter a letter").lower()
    for position in range(len(secret_word)):
        if secret_word[position]==guess:
            display_word[position]=guess
            print(display_word)
    if guess not in secret_word:
        chances -= 1
    if chances == 0:
        print(f"Better Luck next time! The word was {secret_word}")
        game_over = True


    if "_" not in display_word:
        print(f'Congratulations, you have won! The word is {secret_word}')
        game_over=True

    


