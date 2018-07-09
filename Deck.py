import random
class Deck:

    def __init__(self):
        self.currentDeck = {
        'hearts':['king','queen','jack','ace','1','2','3','4','5','6','7','8','9','10'],
        'diamonds':['king','queen','jack','ace','1','2','3','4','5','6','7','8','9','10'],
        'clubs':['king','queen','jack','ace','1','2','3','4','5','6','7','8','9','10'],
        'spades':['king','queen','jack','ace','1','2','3','4','5','6','7','8','9','10']
        }
    
    def __str__(self):
        return str(self.currentDeck)
        
    def cardCount(self):
        return len(self.currentDeck['hearts']) + len(self.currentDeck['diamonds']) + len(self.currentDeck['clubs']) + len(self.currentDeck['spades'])

    def dealCard(self):
        dealtCard = self.randomCard()
        self.removeCard(dealtCard)
        return dealtCard
    
    def randomCard(self):
        suits = []
        for s in self.currentDeck.keys():
            suits.append([s])

        selectedSuit = random.choice(suits)[0]
        selectedFace = random.choice(self.currentDeck[selectedSuit])
        #return a tuple of the card
        return (selectedSuit,selectedFace)
    
    def removeCard(self,card):
        pass
        #remove card from deck
        #self.currentDeck[card(0)].remove(card(1))
        