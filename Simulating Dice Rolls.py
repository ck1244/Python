COST_PER_GAME = 6

def totalScore (dice):#dice = number of dice
    
    
	import random
    
    totalScore =0
	#to generate a random number in a given range (1-6):
	for die in range (dice):
        totalScore += random.randint(1,7)
        
    return totalScore

def Percent (part,whole):
    percentage = round((part/whole)*100)
    return percentage

def Winnings (rolls):
    #how much did i spend assuming its a flat fee per fame (Flat fee * number of rolls)
    expenditure = COST_PER_GAME * rolls
    
    #for every score ("winnings") we need to multiply by the occurances and keep track of the total
    totalWinningsOrLoss = 0
    for score, occurences in count.items():
        totalWinningsOrLoss += score * occurences
    

    #if the total is more than the expenditure i made a profit, otherwise i made a loss
    if totalWinningsOrLoss > expenditure:
        print ("You made a profit")
        print (totalWinningsOrLoss)


def diceRolls ():
    #keep asking the user to enter the number of rolls and dice until they enter zero dice
    while keepGoing ==True:
        count = ()
        dice = int(input("How many dice"))
        if dice ==0:
            break
        rolls = int(input ("How many rolls:"))
        
        for roll in range(0,rolls,1):
            total=totalScore(dice)
            if total in count:
                count[total] += 1
            else:
                count [total] =1
        
        macsxore=6 * dice 
        for score in range (dice,maxscore+1, 1):                              
        percentageOccurances = percent (count[score],rolls)
        print ("%2i : %2i : %% :%s" % (score))
        
        ''' Test code to see the contents of the dictionary
        for k, v in count.items():
            print (k,v)'''
count - ()
            