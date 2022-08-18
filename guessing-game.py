retry = 'y'
numWins = 0
numLosses = 0
wordList = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'farkleberry', 'grape', 'hackberry', 'imbe', 'jackfruit']

while retry == 'y':
    # Game start message
    print('\nGuess the word to win!')

    # Word is chosen
    properChoice = 0
    listLen = len(wordList)
    while properChoice == 0:   
        randomWord = int(input(f'\nChoose a number from a range of 1 to {listLen}: ')) - 1
        try:
            if randomWord < 0:
                print(f'\nPlease choose a number from a range of 1 to {listLen}.')
            elif randomWord > 9:
                print(f'\nPlease choose a number from a range of 1 to {listLen}.')
            else:
                properChoice = 1
        except ValueError:
            print('\nInput needs to be an integer.')
    chosenWord = wordList[randomWord]
    wordList.remove(chosenWord)
    wordLetters = list(chosenWord)
    hintBar = ['_' for i in wordLetters]
    # print(hintBar)

    # Player is given 7 total guesses
    numGuess = 7
    print(f'\nYou have {numGuess} total guesses.')

    while numGuess >= 1:    
    # Player chooses whether to guess a letter or whether to guess the full word
        playerChoice = input("\nType 'l' to choose a letter, or 'f' to choose the full word: ").strip().lower()
        try:    
            print(f'\nYou currently have {numGuess} guesses left.')
            if playerChoice == 'l':
                print('\nYou have decided to choose a letter.')
                # Player chooses what letter to guess
                letterChoice = str(input('Type a letter to make a choice: ').strip().lower())
                try:    
                    if chosenWord.find(letterChoice) == -1:
                        print('\nWrong guess, try again!')
                        numGuess = numGuess - 1
                    # prints out the successful hints in a list format
                    else:
                        for i in range(len(wordLetters)):
                            if wordLetters[i] == letterChoice:
                                hintBar[i] = letterChoice
                        print(f'\n{hintBar}')
                # except len(letterChoice) > 1:
                #     print('\nPlease type a single letter.')
                except ValueError:
                    print('\nThis value must be a string.')
            elif playerChoice == 'f':
                print('\nYou have decided to choose a full word.')
                # Player chooses what full word to guess
                wordChoice = input('Type a full word to make a choice: ').strip().lower()
                try:    
                    if wordChoice == chosenWord:
                        print('\nCongratulations! You won.')
                        numWins = numWins + 1
                        break
                    else:
                        print('\nWrong guess, try again!')
                        numGuess = numGuess - 1
                except ValueError:
                    print('\nThis value must be a string.')        
            else:
                print("\nPlease select either 'l' or 'f'.")
        except playerChoice != ('l', 'f'):
            print("\nPlease type either 'l' or 'f'.")
        except ValueError:
            print('\n Input needs to be a string.')

    if numGuess == 0:
        print('\nBetter luck next time! You lost.\nRoll credits!')
        numLosses = numLosses + 1
    else:
        print('\nRoll credits!')

    retry = input('\nWould you like to play again (y/n)? ').strip().lower()
    try:
        print(f'\nAlright! Your current record is {numWins}:{numLosses} Win/Loss.')
    except retry != ('y','n'):
        print("\nPlease type either 'y' or 'n'.")
    except ValueError:
        print('\nInput needs to be a string.')
