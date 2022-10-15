# Card

class Card:
    values = [None,None,'2','3','4','5','6','7','8','9','10',
            "Jack","Queen","King","Ace"]
    suits = ["Clubs","Diamonds","Hearts","Spades"]
  
    def __init__(self, val, s):
        from random import randint
      
        self.__isAce = False
        self.__aceOne = False
        #self.__value = randint(0, 13)
        self.__value = val
        #s = randint(0,3)
        self.__suitValue = s 
        self.__rank = self.values[self.__value]
        if self.__value == 12:
            self.__isAce = True   
        self.__suit = self.suits[s]
    
    def __repr__(self):
        v = format(self.__rank, "2") + " of " + self.__suit
        return v
    
    def __gt__(self, card2):
        if self.getValue() > card2.getValue():
            return True
        if self.getValue() == card2.getValue():
            if self.getSuitValue() > card2.getSuitValue():
                return True
        else:
            return False
    def __lt__(self, card2):
        if self.getValue() < card2.getValue():
            return True
        if self.getValue() == card2.getValue():
            if self.getSuitValue() < card2.getSuitValue():
                return True
        else:
            return False
    
    def isAce(self):
        return self.__isAce
    
    def aceOne(self):
        return self.__aceOne
    
    def aceSwitch(self):
        if self.__isAce == True:
            if self.__aceOne == True:
                self.__value = 15
                self.__aceOne = False
            elif self.__aceOne == False:
                self.__value = 1
                self.__aceOne = True

    def getValue(self):
        return self.__value
    def getSuitValue(self):
        return self.__suitValue
    def getSuit(self):
        return self.__suit

# Deck

class Deck():

    def __init__(self):
        self.__deck = []
        for i in range(0,4):
            for j in range(2,15):
                card = Card(j, i)
                self.__deck.append(card)
        
                
    def shuffle(self):
        from random import shuffle
        shuffle(self.__deck)

    def deal(self):
        return self.__deck.pop()

    def getCards(self):
        return len(self.__deck)
    
    def showCards(self):
        for i in self.__deck:
            print(i)

    def __repr__(self):
        return "Deck\t" + str(self.getCards()) + " cards left."

# Player

class Player():
    '''
Finish Values: 0: High Card, 1: One Pair,
2: Two Pair, 3: Three of a kind, 4: Straight,
5: Flush, 6: FullHouse, 7: 4 of a kind, 8: StraightFlush
    '''
    finishValues = {0: "High Card", 1: 'One Pair', 2: 'Two Pair',
                3: 'Three of a kind', 4: 'a Straight', 5: 'a Flush',
                6: 'a fullHouse', 7: '4 of a kind', 8: 'a straight flush',
                9: 'a royal flush!'}

    def __init__(self, name, money = 1000):
        self.__name = name
        self.__money = money
        # Stuff to clear
        self.__hand = []
        self.__bet = 0
        self.__highCard = None
        self.__highPairValue = None
        self.__pairList = []
        self.__straight = False
        self.__flush = False
        self.__fullHouse = False
        self.__threeKind = False
        self.__fourKind = False
        self.__twoPair = False
        self.__onePair = False
        self.__finishValue = 0
        
    def __repr__(self):
        return self.__name

    def clearHand(self):
        self.__hand = []
        self.__bet = 0
        self.__highCard = None
        self.__highPairValue = None
        self.__pairList = []
        self.__straight = False
        self.__flush = False
        self.__fullHouse = False
        self.__threeKind = False
        self.__fourKind = False
        self.__twoPair = False
        self.__onePair = False
        self.__finishValue = 0
        
    def refreshHand(self):
        self.__highCard = None
        self.__highPairValue = None
        self.__pairList = []
        self.__straight = False
        self.__flush = False
        self.__fullHouse = False
        self.__threeKind = False
        self.__fourKind = False
        self.__twoPair = False
        self.__onePair = False
        self.__finishValue = 0
        
    def getHand(self):
        return self.__hand

    def getFullHouse(self):
        return self.__fullHouse

    def getFlush(self):
        return self.__flush
    
    def getThreeKind(self):
        return self.__threeKind

    def getFourKind(self):
        return self.__fourKind

    def getTwoPair(self):
        return self.__twoPair
    
    def getOnePair(self):
        return self.__onePair
    
    def dealHand(self, deck):
        for i in range(5):
            card = deck.deal()
            self.__hand.append(card)

    def sortHand(self):
        self.__hand.sort()

    def printHand(self):
        for i in self.__hand:
            print(i)
            
    def discardCard(self, card):    # card is the number for the index in the hand
        del self.__hand[card]
        
    def drawCard(self, deck):
        card = deck.deal()
        self.__hand.append(card)

    def getMoney(self):
        return self.__money
    
    def setHighCard(self):
        self.__hand.sort()
        for i in self.__hand:
            if i not in self.__pairList:
                self.__highCard = i
            
    def getHighCard(self):
        return self.__highCard

    def getHighPair(self):
        return self.__highPairValue

    # Checking the cards
    '''
use board as a parameter for checking the hand
board is the list of cards on the board
playerHandList list contains the board and their hand
check the player hand against each card on the board
when checking 'Flush' 
    '''
    def checkPair(self):
        for i in range(0,len(self.__hand)-1):
            for j in range(i+1, len(self.__hand)):
                if self.__hand[i].getValue() == self.__hand[j].getValue()\
                and self.__hand[i] not in self.__pairList:
                    self.__pairList.append(self.__hand[i])
                if self.__hand[i].getValue() == self.__hand[j].getValue()\
                   and self.__hand[j] not in self.__pairList:
                        self.__pairList.append(self.__hand[j])
        return self.__pairList
    
    def getPairs(self):
        count1 = 0
        count2 = 0
        if not self.__pairList: return
        for i in range(0, len(self.__pairList)):
            if self.__pairList[0].getValue() == self.__pairList[i].getValue():
                count1 += 1
            else:
                count2 += 1
# Set the high pair Value        
        if count2 > count1:
            self.__highPairValue = self.__pairList[-1].getValue()
        elif count2 == 0 or count1 == 2 == count2:
            temp = max(self.__pairList)
            self.__highPairValue = temp.getValue()
        else:
            self.__highPairValue = self.__pairList[0].getValue()
        
        
            
        self.__fullHouse = count1 + count2 == 5
        self.__threeKind = count1 == 3 and count2 == 0
        self.__fourKind = count1 == 4
        self.__twoPair = count1 == 2 == count2
        self.__onePair = count1 == 2 and count2 == 0
        # print("count1",count1,"\tcount2",count2)
        return self.__pairList

    def setStraight(self):
        count = 1
        for i in range(1, len(self.__hand)):
            if self.__hand[0].getValue() + count == self.__hand[i].getValue():
                self.__straight = True
                count +=1
            else:
                self.__straight = False
                break
    
    def getStraight(self):
        return self.__straight

    def setFlush(self):
        for i in range(1, len(self.__hand)):
            if self.__hand[0].getSuitValue() == self.__hand[i].getSuitValue():
                self.__flush = True
            else:
                self.__flush = False
                break

    def getFlush(self):
        return self.__flush
    
    def appendHand(self, card):
        self.__hand.append(card)

    def finish(self):
        if self.__straight and self.__flush:
            if max(self.__hand).getValue() == 14:
                self.__finishValue = 9
            else: self.__finishValue = 8
        elif self.__fourKind:
            self.__finishValue = 7
        elif self.__fullHouse:
            self.__finishValue = 6
        elif self.__flush:
            self.__finishValue = 5
        elif self.__straight:
            self.__finishValue = 4
        elif self.__threeKind:
            self.__finishValue = 3
        elif self.__twoPair:
            self.__finishValue = 2
        elif self.__onePair:
            self.__finishValue = 1
        else:
            self.__finishValue = 0

        return self.__finishValue

# Game Functions
'''
def compare(p1,p2):
    if p1.finish() > p2.finish():
        return p1
    elif p1.finish() < p2.finish():
        return p2
    
    elif p1.finish() == p2.finish():
        if p1.finish() in [1,2,3,6]:
            if p1.getHighPair() > p2.getHighPair():
                return p1
            else:
                return p2
             
        if p1.finish() in [0,1,2,4,5,8]:
            if p1.getHighCard() > p2.getHighCard():
                return p1
            else:
                return p2
    else:
        return 'draw'
'''
def compare(playerList):
    splitList = [playerList[0]]
    length = len(playerList)
    
    for i in range(0, length):
        if playerList[i] not in splitList:
            break
        for j in range(i + 1,len(playerList)-1):
            if playerList[i] not in splitList:
                break
            if playerList[i].finish() > playerList[j].finish():
                del playerList[j]
                continue
            elif playerList[i].finish() == playerList[j].finish():
                tie = getTie(playerList[i], playerList[j])
                if tie == 'draw': splitList.append(playerList[j])
                elif tie == playerList[i]: continue
                else:
                    del playerList[i]
                    splitList = []
                    splitList.append(playerList[j])
            else:
                del playerList[i]
                splitList = []
                splitList.append(playerList[j])
                break
    return splitList
            
def getTie(p1,p2):
    pairList = [1,2,3,7]
    highCardList = [0,4,5,6,8,9]
    if p1.finish() in pairList:
        if p1.getHighPair() > p2.getHighPair(): return p1
        elif p1.getHighPair() == p2.getHighPair():
            if p1.getHighCard() == p2.getHighCard(): return 'draw'
            elif p1.getHighCard() > p2.getHighCard(): return p1
            else: return p2
    if p1.finish() in highCardList:
        if p1.getHighCard() == p2.getHighCard(): return 'draw'
        elif p1.getHighCard() > p2.getHighCard(): return p1
        else: return p2

    
def draw(player, deck):
    transfer = []
    throwAway = []
    throwAway = input("Enter the number of the cards to \
discard or press enter: ")
    if throwAway == '': return
    else:
        for i in throwAway.split(','): transfer.append(int(i))
        drawNumber = len(transfer)
    transfer.sort()
    
    for i in range(0, drawNumber): player.discardCard(transfer.pop()-1)

    for j in range(drawNumber): player.drawCard(deck)
    

        
        

# Functions for testing hands

def randomDeals(p1):    
    while True:
        print()
        
        p1.clearHand()
        deck = Deck()
        deck.shuffle()

        p1.dealHand(deck)
        p1.sortHand()
        p1.printHand()

        printResults(p1)
        print("--------------------------")
        print()
        
        
        
        n = input("q to quit")
        if n == 'q':
            break
    
def dealFullHouse(p1):
    p1.clearHand()
    one =Card(4,0)
    two = Card(4,1)
    three = Card(5,0)
    four = Card(5,2)
    five = Card(5,3)
    p1.appendHand(one)
    p1.appendHand(two)
    p1.appendHand(three)
    p1.appendHand(four)
    p1.appendHand(five)
    p1.printHand()

    
def dealThreeKind(p1):
    p1.clearHand()
    one =Card(2,0)
    two = Card(11,1)
    three = Card(11,2)
    four = Card(11,0)
    five = Card(3,3)
    p1.appendHand(one)
    p1.appendHand(two)
    p1.appendHand(three)
    p1.appendHand(four)
    p1.appendHand(five)
    p1.printHand()

def dealTwoPair(p1):
    p1.clearHand()
    one =Card(2,0)
    two = Card(4,1)
    three = Card(2,2)
    four = Card(4,2)
    five = Card(9,3)
    p1.appendHand(one)
    p1.appendHand(two)
    p1.appendHand(three)
    p1.appendHand(four)
    p1.appendHand(five)
    p1.printHand()
    
    
def printResults(p1):
    print()
    print("Like Cards:",p1.checkPair())
    p1.getPairs()
    p1.setHighCard()
    print("High Card:",p1.getHighCard())
    print("One Pair:", p1.getOnePair())
    print("Two Pair:", p1.getTwoPair())
    print("Three of a kind:",p1.getThreeKind())
    print("Straight: ",p1.setStraight())
    print("Flush: ",p1.setFlush())
    print("Four of a Kind: ",p1.getFourKind())
    print("Full House: ",p1.getFullHouse())
    print("High Pair Value:",p1.getHighPair())
    print("Finish Value:",p1.finish())
    print()
    
def getResults(p1):
    p1.checkPair()
    p1.getPairs()
    p1.setHighCard()
    p1.setFlush()
    p1.setStraight()
    p1.getHighPair()
    return p1.finish()
   
    
def main():
    p1 = Player("Tim")
    p2 = Player("John")
    p3 = Player("Jack")
    players = [p1, p2, p3]

    while True:
        deck = Deck()
        deck.shuffle()
        for i in players:
            i.clearHand()
            i.dealHand(deck)
            getResults(i)
            print("Player:",i)
            print("You have", i.finishValues[getResults(i)])
            
            i.printHand()
            draw(i, deck)
            i.refreshHand()
            getResults(i)
            print("Player:",i)
            print("You have", i.finishValues[getResults(i)])
          
            i.printHand()
            input("Press Enter")
            print("-----------------")
        winner = compare(players)
        print("Winner:", winner[0], "with", winner[0].finishValues[getResults(i)])
        if input("q to quit") == 'q': break
        print()


        
main()
