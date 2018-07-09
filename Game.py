class Game:   
#Rules*******************************************
#Blackjack starts with players making bets.
#Dealer deals 2 cards to the players and two to himself (1 card face up, the other face down).
#Blackjack card values: All cards count their face value in blackjack. Picture cards count as 10 and the ace can count as either 1 or 11. Card suits have no meaning in blackjack. The total of any hand is the sum of the card values in the hand
#Players must decide whether to stand, hit, surrender, double down, or split.
#The dealer acts last and must hit on 16 or less and stand on 17 through 21.
#Players win when their hand totals higher than dealer’s hand, or they have 21 or less when the dealer busts (i.e., exceeds 21).
#Rules*******************************************    
    def __init__(self,players=1):
        self.players = players
        #map points to cards
        #Aces can be high or low
        self.pointsMapping = {
            'king':10,
            'queen':10,
            'jack':10,
            'ace':1, #can be 1 or 11
            '10':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,
            '4':4,
            '3':3,
            '2':2,
            '1':1
        }
        
        #build player list starting with house
        self.playerList = ['house']
        p = 1
        while p <= self.players:
            self.playerList.append(str(p))
            p+=1
        
    
        #set player scores
        #playerScores = {}
        #p=1
        #while p <= self.players:
            #playerScores.update({str(p):0})
            #p+=1
        #add house score
        #playerScores.update({'house':0})
        
        #create class variable
        self.playerCards = {}
        
        for i in self.playerList:
            self.playerCards[i]=[]
        
        #hand = [
        #    {'Pat': [('clubs','1'),('spades','5')]},
            
        #]
        
    def __str__(self):
        return str(self.playerCards)
        
    def start(self):
        gameOver = False
        while gameOver == False:
            pass

        else:
            print('Game over!')
            
    def firstDeal(self):
        #create new deck
        d = Deck()
        print('New deck created!')
        
        #now deal 2 cards to all players, including the house
        #set player cards
        dealNum = 1
        while dealNum <= 2:
            for p in self.playerList:
                dealtCard = d.dealCard()
                print("Dealt card: {}".format(dealtCard))
                self.addCardToHand(p,dealtCard)
            dealNum+=1
            
    def secondDeal(self):
        #deals the third card
        pass
    
    def thirdDeal(self):
        #deals the fourth card
        pass
    
    def fourthDeal(self):
        #deals the fifth card
        pass
        

    

        