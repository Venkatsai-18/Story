import random 
from stages import display_hangman

words=[
        "ball",
        "paper",
        "car",
        "bike",
        "collage",
        "pencil",
        "hero",
        "google",
        "super",
        "winter",
        "india",
        "delhi",
        "maggie",
        "master",
        "watch",
        "light",
        "king",
        "ground",
        "viratkohli",
        "raina",
        "dhoni",
        "pink",
        ]
            
    
def get_word():
    word= random.choice(words)
    return word.lower()

def play(word):
    word_complete="_"*len(word)
    guessed=False
    tries=6
    score=0
    guessed_letters=[]
    guessed_words=[]
    print("Let's play Hangman")
    display_hangman(tries)
    print(word_complete)
    print("\n")
    while not guessed and tries>0:
        guess=input("please guess a letter or a lettern or word : ").lower()
        score+=1
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"already you guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in word")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("good job")
                guessed_letters.append(guess)
                ls=[]
                word_as_list=list(word_complete)
                for i in range(len(word)):
                    if word[i]==guess:
                        ls.append(i)

                for i in range(len(word_complete)):
                    if i in ls:
                        word_as_list[i]=guess
                word_complete="".join(word_as_list)
                if "_" not in word_complete:
                    guessed=True

        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess!=word:
                print(f"{guess} is not the word")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_complete=guess
                
        else:
            print("### Not a valid guess")
        display_hangman(tries)
        print(word_complete)
        print("\n")
    if guessed:
        print(f"Congrats! you gueesed the word score = {score}")
    else:
        print(f"Better luck next time! You ran out of tries. The word was {word}")
        
def main():
    word=get_word()
    play(word)
    while input("Play again ? (Y/N)").upper()=="Y":
        word=get_word()
        play(word)       
        
if __name__=="__main__":
    main()

