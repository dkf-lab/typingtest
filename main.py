import random
import time
sentence = []
score = 0
wpm = 0
averagewpm = 0
round = 1
while True:
    sent = input("Enter sentence:")
    if sent == "":
        break
    sentence.append(sent)
while True:
    lensent = len(sentence) - 1 #figure out how long the list is, and then adjusting for line 5
    x = (random.randint(0, lensent)) #random number, determines what sentence comes up
    print(sentence[x]) #print sentence
    start = time.time() #start timer
    sentlength = len(sentence[x]) #defines length of sentence
    usrinput = input() #get user input
    if usrinput == 'exit':
        print('Exiting! Your final score was',score,'and your average WPM was',int((averagewpm/round)))
        break
    else:
        if usrinput == sentence[x]:
            end = time.time()
            wpm= (sentlength/(end-start)/5*60)
            score += 1
            round += 1
            averagewpm += wpm
            print("Correct! Your WPM was",int(wpm),"and your score is currently",score)
        else:
            if score == 0:
                print("Incorrect! Your score is now",score)
            else:
                score -=1
                print("Incorrect! Your score is now",score)
