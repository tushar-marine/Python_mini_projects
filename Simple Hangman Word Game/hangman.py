import time
import random

# initial steps to invite in the game:
print('Welcome to Hangman game...\n')
name = input('Enter your name: ')
print('Hello ' + name + '! Best of Luck!!!')
time.sleep(2)
print('Starting the game...\n')
time.sleep(3)

def main():
    global count
    global display
    global word
    global guessed
    global length
    global play
    global checker
    global ans
    global done

    word_list = ["abiu", "acerola", "ackee", "apple", "apricot", "avocado", "banana", "bilberry",
                 "blackberry", "blackcurrant", "blueberry", "boysenberry", "breadfruit", "cherry",
                 "cherimoya", "cloudberry", "coconut", "cranberry", "damson", "date", "dragonfruit",
                 "durian", "grape", "guava", "honeyberry", "huckleberry", "jackfruit", "kiwifruit",
                 "kumquat", "lemon", "lime", "lychee", "mango", "melon", "cantaloupe", "honeydew",
                 "watermelon", "mulberry", "orange", "clementine", "tangerine", "papaya", "passionfruit",
                 "peach", "pear", "persimmon", "plantain", "plum", "pineapple", "pineberry", "raspberry",
                 "salmonberry", "strawberry", "tamarind", "tangelo", "tayberry", "tomato", "yuzu"]
    word = random.choice(word_list)
    length = len(word)
    count = 0
    display = ''
    i = 0
    checker = []
    while i<length:
        checker.append(1)
        if i>0:
            display+=' _'
        else:
            display+='_'
        i+=1
    guessed = []
    play = ''
    ans = word.strip()
    done = 0
# option to play again
def play_loop():
    play = input('Play again? Press Y/N\n')
    while play not in ['Y', 'y', 'N', 'n']:
        play = input('Play again? Press Y/N\n')

    if play == 'Y' or 'y':
        main()
    else:
        print('Thank you for playing!!!\n')
        time.sleep(3)
        exit()

# Initializing all the conditions required for the game:
def game():
    global count
    global display
    global word
    global guessed
    global play_game
    global checker
    global ans
    global done
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip() # input String

    if len(guess.strip()) == 0:
        print("No input detected!!! Try a letter\n")
        game()

    elif len(guess.strip()) >1:
        print("More than one input!!! Enter any single letter\n")
        game()

    elif not str.isalpha(guess.strip()):
        print("Invalid Input, Try a letter\n")
        game()

    elif guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        if checker[index] == 1:
            word = word[:index] + "_" + word[index + 1:]
            if index == 0:
                display = display[:index] + guess + display[index + 1:]
            else:
                display = display[:index+index] + guess + display[index + index + 1:]
            print(display + "\n")
            checker[index] = 0
            done+=1

    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |  " + str(limit - count) + "  | \n"
                  "  |_____|\n")
            print("Wrong guess! " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |  " + str(limit - count) + "  | \n"
                  "  |_____|\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |  " + str(limit - count) + "  | \n"
                  "  |_____|\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |  " + str(limit - count) + "  | \n"
                  "  |_____|\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("    _____ \n"
                  "  |  " + str(limit - count) + "  | \n"
                  "  |_____|\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", guessed, word)
            print('Game Over!!!')
            time.sleep(2)
            play_loop()

    if done == length:
        print("Congrats! You have guessed the word correctly!")
        print('You have guessed, \'' + ans + '\'')
        print('Game Over!!!')
        time.sleep(2)
        play_loop()
    elif count != limit:
        game()
main()
game()



