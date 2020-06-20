import random
import time
import os
#function for clearing console
def clearLines():
    for _  in range(3):
        print('')
clearScreen = lambda: os.system('cls')
#define various varibles/lists we will be using later.
prompteduser = 0
sentence = []
score = 0
wpm = 0
averagewpm = 0
round = 1

#Selecting a sentence list

while True:
    if prompteduser == 0:
        print("Type 'external' to use sentences.dat or press enter to exit.")
        prompteduser=1
    sent = input("Enter sentence:")
    if sent == "":
        break
    if sent == 'external':
        text_file = open("sentences.dat")
        lines = text_file.read().splitlines() #or use split(seperator)
        sentence = lines
        text_file.close()
        break
    sentence.append(sent)

#The game itself

while True:
    lensent = len(sentence) - 1 #figure out how long the list is, and then adjusting for line 5
    x = (random.randint(0, lensent)) #random number, determines what sentence comes up
    print(sentence[x]) #print sentence
    start = time.time() #start timer
    sentlength = len(sentence[x]) #defines length of sentence
    usrinput = input() #get user input
    if usrinput == 'exit':
        clearScreen()
        clearLines()
        print('Exiting! Your final score was',score,'and your average WPM was',int((averagewpm/round)))
        break
    else:
        if usrinput == sentence[x]:
            end = time.time()
            wpm= (sentlength/(end-start)/5*60)
            score += 1
            round += 1
            averagewpm += wpm
            print('')
            print("Correct! Your WPM was",int(wpm),"and your score is currently",score)
            clearLines()
        else:
            if score == 0:
                print('')
                print("Incorrect! Your score is now",score)
                clearLines()
            else:
                score -=1
                print('')
                print("Incorrect! Your score is now",score)
                clearLines()
