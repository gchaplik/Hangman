import random


word= random.choice(open("words.txt").read().split())
word=word.lower()
yourWord = [char for char in word]
check = ['_' for char in word]
outs=['o'for i in range(7)]
used=set({})
count = 0
continueGame = 'y'
startGame='n'
print("Your Word contains ",len(check)," letters ",check)
while(continueGame=='y'):
    if(startGame=='y'):
        word= random.choice(open("words.txt").read().split())
        word=word.lower()
        yourWord = [char for char in word]
        check = ['_' for char in word]
        outs=['o'for i in range(7)]
        print("Your Word contains ",len(check)," letters ",check)
        count=0
        used=set({})
        startGame='n'
    yourGuess = input("Please input a letter from A-Z (Not Case sensitive))").lower()
    used.add(yourGuess)
    
    if(yourGuess.strip() in yourWord):
        for i in range(len(yourWord)):
            if(yourWord[i]==yourGuess):
                check[i]=yourGuess

                
    else:
        outs.pop()
        outs.insert(count,'X')
        count+=1
        
    
    print("You have found ",len(check)-check.count('_'),"out of",len(check),"letters",check)
    print("You have ",len(outs)-outs.count('o'),"/",len(outs),"lives left",outs)
    print("USED LETTERS:", used,"\n")
    if('o' not in outs or '_'not in check):
        if('o' not in outs):
            print("The word was",word)
        if('_' not in check):
            print("YOU WON !!!",word)
        continueGame=input("would you like to continue? (y/n)").lower()
        if(continueGame=='n'):
            print("Thank you for playing!!")
        startGame='y'
