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
        #Game stuff
        self.__name = name
        self.__money = money
        # Stuff to clear
        self.__hand = []
        self.__bet = 0
        self.__totalBet = 0
        self.__highCard = None
        self.__highPairValue = None
        self.__pairList = []
        # Clear these every betting round
        self.__call = False
        self.__fold = False
        self.__raise = False
        # Hands
        self.__straight = False
        self.__flush = False
        self.__fullHouse = False
        self.__threeKind = False
        self.__fourKind = False
        self.__twoPair = False
        self.__onePair = False
        # Ai
        self.__ai = False
        self.__finishValue = 0
        
    def __repr__(self):
        return self.__name
    
    # Hand and Bet Methods
    
    def clearHand(self):
        self.__hand = []
        self.__bet = 0
        self.__call = False
        self.__fold = False
        self.__raise = False
        self.__highCard = None
        self.__highPairValue = None
        self.__pairList = []
        # Hands
        self.__straight = False
        self.__flush = False
        self.__fullHouse = False
        self.__threeKind = False
        self.__fourKind = False
        self.__twoPair = False
        self.__onePair = False
        
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

    def getMoney(self):
        return self.__money
    
    def getHand(self):
        return self.__hand

    def getBet(self):
        return self.__bet
    
    def getTotalBet(self):
        return self.__totalBet

    def getCall(self):
        return self.__call

    def setCall(self):
        self.__call = True

    def getRaise(self):
        return self.__raise

    def setRaise(self):
        self.__raise = True

    def getFold(self):
        return self.__fold

    def setFold(self):
        self.__fold = True
    
    def clearBet(self):
        self.__bet = 0

    def bet(self):
        self.__bet = getMoney()
        self.__totalBet += self.__bet
        if self.__bet >= self.__money:
            self.__bet = self.__money
        self.__money -= self.__bet
        return self.__bet
    
    def call(self, currentBet):
        self.__bet = currentBet
        self.__totalBet += self.__bet
        if self.__bet >= self.__money:
            self.__bet = self.__money
        self.__money -= self.__bet
        self.__call = True
        return self.__bet
    
    def win(self, amount):
        self.__money += amount
        
    # Possible Hands

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
            
    # Hand and Card Actions 

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
    
    def setHighCard(self):
        self.__hand.sort()
        for i in self.__hand:
            if i not in self.__pairList:
                self.__highCard = i
            
    def getHighCard(self):
        return self.__highCard

    def getHighPair(self):
        return self.__highPairValue
    
    # AI methods

    #def aiCheck(self):
    
    def setAi(self):
        self.__ai = True
        
    def getAi(self):
        return self.__ai
        
    def aiGetFaceCard(self, card):
        if card.getValue() > 10: return True
        
    def aiFlush(self):
        for i in range(0,2):
            flushList = [self.__hand[i]]
            match = 1
            count = 0
            for j in range(1, len(self.__hand)):
                if self.__hand[i] == self.__hand[j]:
                    continue
                if self.__hand[i].getSuitValue() ==\
                   self.__hand[j].getSuitValue():
                    match += 1
                    flushList.append(self.__hand[j])
                else:
                    count += 1

                if count == 2:
                    flushList = []
                    break
                if match == 4:
                    return flushList
        return           
        
    def aiStraight(self):
        straight = 0
        step = 0
        gap = 0
        self.__hand.sort()
        count = 0
        countMax = 0
        for i in range(0, 2):
            straightList = []
            straightList.append(self.__hand[i])
            for j in range(1, len(self.__hand)):
                if self.__hand[j].getValue() ==\
                self.__hand[i].getValue() + j:
                    straight += 1
                    straightList.append(self.__hand[j])
                    count += 1
                elif self.__hand[j].getValue() ==\
                self.__hand[i].getValue() + 1 + j:
                    step += 1
                    count = 0
                    straightList.append(self.__hand[j])
                else:
                    if i >= 1 and count < 3:
                        break
                    gap +=1
                    count =0
                    straightList = []
        if count == 3: return straightList
                      
    def aiSetDiscard(self, list):
        discardList = []
        for i in range(0, len(self.__hand)):
            if self.__hand[i] in list:
                continue
            else:
                discardList.append(self.__hand.index(self.__hand[i]))
        discardList.sort
        return discardList    
            
    def aiPairs(self):
        keepList = []
        if self.__pairList:
            for i in range(0, len(self.__pairList)):
                keepList.append(self.__pairList[i])
        if self.aiGetFaceCard(self.__highCard) and len(self.__pairList) < 3:
            keepList.append(self.__highCard)        
        return keepList     
        
# Checking and processing the cards
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

#Game Class
    
class Game:
    
    def __init__(self, playerList):
        self.__playerList = playerList
        self.__handList = []
        self.__firstBet = playerList[0]
        self.__firstBetIndex = 0
        self.__ante = 0
        # to be cleared
        self.__pot = 0
        self.__currentBet = 0
        self.__round = 0
        self.__deck = Deck()

    def getDeck(self):
        return self.__deck

    def getPlayer(self, number):
        return self.__playerList[number]
    
    def shuffleDeck(self):
        self.__deck = Deck()
        self.__deck.shuffle()
        
    def getPlayerList(self):
        return self.__playerList

    def getPlayerTotal(self):
        return len(self.__playerList)
    
    def getHandList(self):
        return self.__handList
    
    def getHandTotal(self):
        return len(self.__handList)

    def addHand(self, player):
        self.__handList.append(player)

    def removeHand(self, player):
        del self.handList[player]

    def clearHand(self):
        self.__handList.clear()

    def getCurrentBet(self):
        return self.__currentBet
    
    def getFirstBetIndex(self):
        return self.__firstBetIndex

    def getPot(self):
        return self.__pot
    
    def setPot(self, amount):
        self.__pot += amount
        
    def getAnte(self):
        return self.__ante
    
    def setAnte(self, amount):
        self.__antee = amount

    def bet(self, player):     
        amount = player.bet()
        if amount > self.__currentBet:
            self.__currentBet = amount
        self.setPot(amount)
        return amount
    
    def call(self, player):
        player.setCall
        player.call(self.__currentBet)
        
    def callRaise(self, player):
        player.call(self.__currentBet)
        print("Enter the amount to raise by: $", end = '')
        self.bet(player)
        
    def fold(self, player):
        player.clearHand()
        self.removeHand(player)
        
    def getFirstBet(self):
        return self.__firstBet

    def setFirstBet(self):
        total = len(self.__handList)
        if self.__playerList.index(self.__firstBet) + 1 == total:
            self.__firstBet = self.__playerList[0]
        else: self.__firstBet = self.__playerList[\
            self.__playerList.index(self.__firstBet) + 1]
        self.__firstBetIndex = self.__playerList.index(self.__firstBet)
        
    def payOut(self, winner):
        winner.win(self.__pot)
        self.__pot = 0
        
    def clearBoard(self):
        self.__pot = 0
        self.__currentBet = 0
        self.clearHand()


        
# Game Functions
def compare(playerList):
    splitList = [playerList[0]]
    count = length = len(playerList)
    while count > 1:
        if playerList[0].finish() > playerList[1].finish():
                del playerList[1]
                
        elif playerList[0].finish() == playerList[1].finish():
            tie = getTie(playerList[0], playerList[1])
            if tie == 'draw':
                splitList.append(playerList[1])
                del playerList[1]
            elif tie == playerList[0]:
                del playerList[1]
            else:
                splitList = []
                splitList.append(playerList[1])
                del playerList[0]
        else:
            splitList = []
            splitList.append(playerList[1])
            del playerList[0]
        count -= 1
    return splitList

def draw(game):
    start = game.getFirstBetIndex()
    for i in range(0, game.getPlayerTotal()):
        playerDraw(game.getPlayer(start))
        if start == game.getPlayerTotal():
            start = 0
        start += 1

def playerDraw(player, deck):
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

def bet(game):
    exit = False
    start = game.getFirstBetIndex()
    while not exit:
        for i in range(0, game.getHandTotal()):
            if not game.getCurrentBet():
                print("Enter your bet, or 0 to check: ", end = '')
                game.bet(game.getPlayer(start).bet())
            elif game.getPlayer(start).getBet() < game.getCurrentBet:
                betMenu(game, game.getPlayer(start))
            if start == game.getHandTotal() -1:
                start = 0
            else: start += 1


def betMenu(game, player):
    print("c for call \nf for fold\nr for call and raise\n")
    print("Current bet: $" + game.getCurrentBet() + ". Your move..? ", end = '')
    choice = None
    while choice not in ['c','f','r']:
        choice = input()
        if choice == 'c':
            game.call(player)
            print(player,"calls")
        elif choice =='f':
            print(player,"folds")
            game.fold(player)
        elif choice =='r':
            amount = game.callRaise(player)
            print(player,"Sees $"+str(game.getCurrentBet()),"and raises $"+str(amount))
        else:
            print("Please make a valid selection (c, f, r): ", end = '')
            
        
                    
                      
            
        

        
##def bet(game):
##    exit = False
##    while not exit:
##        start = game.getFirstBetIndex()
##        for i in range(0, game.getPlayerTotal()):
##            if game.getPlayer(start).getBet() == game.getPlayer(start - (game.getPlayerTotal() - 1)):
##                exit = True
##                continue
##            print("Player: ", game.getPlayer(start))
##            if game.getCurrentBet():
##                print("Current bet: $" + str(game.getCurrentBet()))
##                while True:
##                    if game.bet(game.getPlayer(start)) < game.getCurrentBet():
##                        print("$" + str(game.getCurrentBet()) + " is the minimum bet.")
##                    else: break
##            else:
##                print("Bets to you...")
##                game.bet(game.getPlayer(start))
##            if start == game.getPlayerTotal() -1:
##                start = 0
##            else: start += 1
##        exit = True
##        for i in range(0, game.getPlayerTotal()):
##            for j in range(1, game.getPlayerTotal()):
##                if game.getPlayer(i).getBet() < game.getPlayer(j).getBet():
##                    start = i
##                    exit = False
##                elif game.getPlayer(i).getBet() < game.getPlayer(j).getBet():
##                    start = j
##                    exit = False
##    print("Pots good...")
        
        
def getHand(player):
    count = 1
    for i in player.getHand():
        print(format(count, "2") + ": " + str(i))
        count +=1

def getMoney():
    while True:
        test = input()
        try:
            int(test)
        except ValueError:
            print("Our smallest chip is $1.")
            continue
    return int(test)
            
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

def iniateGame():
    players = []
    name = input("Enter your name: ")
    p1 = Player(name)
    a1 = Player("Test1")
    a2 = Player("Test2")
    players.append(p1)
    players.append(a1)
    players.append(a2)
    return players


        
# Header PRINT functions
def playerHeader(player):
    print("#"*40)
    print("Player:",player, end='  ***  ')
    print("You have", player.finishValues[getResults(player)])
    print("#"*40)

def aiHeader(player):
    print("#"*40)
    print("AI Player:",player,)
    print("#"*40)

def finalHeader(player):
    print("#"*40)
    print("\t",player, "has", player.finishValues[getResults(player)])
    getHand(player)
    print("#"*40)

def winnerHeader(player):
    print("#"*40)
    print("\t",player, "wins with", player.finishValues[getResults(player)])
    getHand(player)
    print("#"*40)

    
# AI FUNCTIONS
def aiDecide(player):
    holdList = [4,5,6,8,9]
    playList = [1,2,3,7]
    handValue = player.finish()
    if handValue in holdList: return
    elif handValue in playList:
        return player.aiPairs()
    elif handValue == 0:
        if player.aiFlush(): return player.aiFlush()
        if player.aiStraight(): return player.aiStraight()
        else: return player.aiPairs()
    
        
def aiDraw(player, list, deck):
    discard = player.aiSetDiscard(list)
    drawAmount = len(discard)
    while discard:
        player.discardCard(discard.pop())
    for i in range(drawAmount):
        player.drawCard(deck)
    print("Discarding",drawAmount,"cards.")
    input()
    
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
    p1.refreshHand()
    p1.checkPair()
    p1.getPairs()
    p1.setHighCard()
    p1.setFlush()
    p1.setStraight()
    p1.getHighPair()
    return p1.finish()
   
    
def main():
    p1 = Player("Tim")
    a1= Player("John")
    a1.setAi()
    a2 = Player("Jack")
    a2.setAi()
    

    while True:
        players1 = []
        players = [p1, a1, a2]
        for i in players:
            players1.append(i)
        deck = Deck()
        deck.shuffle()
        for i in players:
            i.clearHand()
            i.dealHand(deck)
            getResults(i)
            
            print()
            if i.getAi():
                aiHeader(i)
                #getHand(i)
                #printResults(i)
                aiDraw(i, aiDecide(i), deck)
                getResults(i)
                #getHand(i)
                #printResults(i)
            else:
                playerHeader(i)            
                getHand(i)
                #printResults(i)
                playerDraw(i, deck)
                getResults(i)
                playerHeader(i)
                getHand(i)
                #printResults(i)
                input("Press Enter")
                print()
        winner = compare(players)
        print("\tResults")
        for i in range(0,len(players1)):
            if players1[i] not in winner:
                finalHeader(players1[i])
        winnerHeader(winner[0])
        
        if input("q to quit") == 'q': break
        print()

def test():
    game = Game(iniateGame())
    for i in game.getPlayerList():
        game.addHand(i)
    bet(game)
        

test()       
#main()
