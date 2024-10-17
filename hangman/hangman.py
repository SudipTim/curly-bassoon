import random

def word_selection():
        with open("data.txt", "r") as f:
              line=f.readlines()
              word=random.choice(line).strip()
              return word
                

def main(word, letters,hidden_word):
    attempts = 7
    score=0
    while attempts > 0:
        print("\nCurrent word:", " ".join(hidden_word))
        guess= input("\nEnter a letter: ").lower().strip()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters:
                for index, letter in enumerate(word):
                    if letter == guess:
                        hidden_word[index] = letter
            else:
                print(f"\nincorrect guess: {guess}") 
                attempts-= 1   
                print(f"attempts left: {attempts}")
        else:
             print("Enter a letter!")        
        if "_" not in hidden_word:
             print(f"\nCongratulations!\nYou guessed the correct word: {word}")
             score+=1
             print(f"score: {score}")
             break
        if attempts == 0:
             print(f"The word was: {word}")
             break

def inputs():
    while True:
        choice=input("Play(1)\nQuit(2)\n: ")
        if choice == "1":
            word=word_selection()
            print(f"length of the word: {len(word)}")
            hidden_word = ["_" for _ in word]
            letters = list(word)
            print(word)
            main(word,letters,hidden_word)


        if choice=="2":
            break

        else:
             print("Enter a valid option")     

        

if __name__ == "__main__":
    inputs()
    
