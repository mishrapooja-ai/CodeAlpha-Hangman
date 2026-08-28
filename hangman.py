import random
#lists of words for game
words=("apple","box","python","tiger","house")

#choose a random secret word
secret_word=random.choice(words)

#creat blanks for each letter
display=["_"]*len(secret_word)
print(" ".join(display))

#game settings
lives=6
guessed_letters=[]
wrong_letters=[]

#display remaining lives
def show_hangman(lives):
    print("Lives",lives)

#main game loop
while "_" in display and lives>0:
    guess=input("Guess the word:").lower()

    #make sure the players enter only one character
    if len(guess)!=1:
        print("Please enter only one letter.")
        continue
    #check for repeated letters
    if  guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    print("You guessed:",guess)
    #check wheteher the letter in secret word
    if guess in secret_word:
        print("You guessed correct") #reveal the correct word
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                display[i]=guess
    else:
        print("You guessed wrong")
        lives=lives-1
        wrong_letters.append(guess)
        print("The wrong letters are:",",".join(wrong_letters))
        print("Remaining Lives:",lives)
    print(" ".join(display))
    show_hangman(lives)

if "_" not in display:     #game result
    print("Congratulations!You Won!")
else:
    print("The game was over")
    print("The word was:",secret_word)