'''
Hangman
By Ryan Slater
July 2017
'''

from PyDictionary import PyDictionary
import random as rand
from nltk.corpus import words

def __makeGuess__():
    '''
    Returns
    ----------
    guess : bool
        Is guess correct or not
    '''
    letter = ''
    guess = True
    print('\nGuess a letter')
    while guess:
        letter = input()
        if len(letter) > 1:
            print('Enter only one character!')
        elif letter in guesses:
            print('You already guessed that!')
        elif letter not in letters:
            print('Enter a single lowercase letter!')
        else:
            break
    print(100*'\n')
    guesses.append(letter)
    if letter in word:
        goodLetters.append(letter)
    else:
        guess = False
    return guess

def __showWord__(word, goodLetters):
    for i in range(len(word)):
        if word[i] in goodLetters:
            print(word[i], end='')
        else:
            print(' _ ', end='')

def __checkWord__():
    checkWord = False
    wordLetters = []
    lettersCorrect = []
    for i in range(len(word)):
        wordLetters.append(word[i])
    for i in range(len(wordLetters)):
        if wordLetters[i] in guesses:
            lettersCorrect.append(True)
        else:
            lettersCorrect.append(False)
    for i in range(len(lettersCorrect)):
        if lettersCorrect[i] == False:
            checkWord = False
            break
        else:
            checkWord = True
    return(checkWord)

def __lifeCounter__(l):
    print('\n')
    if l == 0:
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('       _____')
    elif l == 1:
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('       _/|\_')
    elif l == 2:
        print('          ')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 3:
        print('     ____')
        print('        \|')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 4:
        print('     ____')
        print('     |  \|')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 5:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 6:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('     |   |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 7:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('     |   |')
        print('     |   |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 8:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('    /|   |')
        print('     |   |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 9:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('    /|\  |')
        print('     |   |')
        print('         |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l == 10:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('    /|\  |')
        print('     |   |')
        print('    /    |')
        print('         |')
        print('         |')
        print('       _/|\_')
    elif l >= 11:
        print('     ____')
        print('     |  \|')
        print('     O   |')
        print('    /|\  |')
        print('     |   |')
        print('    / \  |')
        print('         |')
        print('         |')
        print('       _/|\_')

def __getWord__():
    validWord = False
    while validWord == False:
        print('Enter word:')
        word = input()
        for i in range(len(word)):
            if word[i] not in letters:
                print(100*'\n' + 'Enter a single word in all lowercase letters!')
                break
            elif i == len(word)-1:
                return(word)

def __getWordFromList__():
    wordList = words.words()
    i = rand.randint(0, len(wordList)-1)
    word = wordList[i]
    while len(word) < 5:
        i = rand.randint(0, len(wordList)-1)
        word = word[i]
    word = word.lower()
    return(word)

def Hangman():
    dictionary = PyDictionary()
    global letters
    global word
    global guesses
    global goodLetters
    letters = 'abcdefghijklmnopqrstuvwxyz'
    winOrLose = False
    userWord = False
    lives = 11
    livesUsed = 0
    guesses = []
    goodLetters = []

    print('How many players?')
    while userWord == False:
        numPlayers = input()
        if numPlayers == '1' or numPlayers == '2':
            int(numPlayers)
            break
        else:
            print('Please enter \'1\' or \'2\'')

    if numPlayers == '1':
        word = __getWordFromList__()
    else:
        word = __getWord__()

    print(500*'\n')
    while userWord == False:
        if livesUsed >= lives:
            break
        __showWord__(word, goodLetters)
        print('\nGuesses: ', end='')
        for i in range(len(guesses)):
            if i == 0:
                print(guesses[i], end='')
            else:
                print(', ' + guesses[i], end='')
        __lifeCounter__(livesUsed)
        guess = __makeGuess__()
        if guess == False:
            livesUsed += 1
        if __checkWord__() == True:
            userWord = True
            winOrLose = True

    __lifeCounter__(livesUsed)
    print(str(word) + "   " + dictionary.meaning(word) + '\n')
    if winOrLose == True:
        print('You Win!')
    else:
        print('You Lose!')
    print(str(len(guesses)) + ' guesses')
    print('Used ' + str(livesUsed) + '/11 lives')
