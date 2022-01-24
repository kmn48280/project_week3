import random 
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# class:
#     dealer
#     player
#     deck of cards (unnecessary)
#     UI

#show instructions
#show the BlackJack table (dealer, player, and deck)
# 52 cards [1-13]-includes face cards; [4]-suits 
#shuffle
# deal
# calculate value of cards
# hit/stand
# evaluate for bust for dealer AND player 
# evaluate for winner b/ween dealer and player 
# clear the table 
# shuffle 
DECK = []
hearts_dict = {
    'AH': 1 or 11,
    '2H': 2,
    '3H': 3,
    '4H': 4,
    '5H': 5,
    '6H': 6,
    '7H': 7,
    '8H': 8, 
    '9H': 9,
    '10H': 10,
    'JH': 10,
    'QH': 10,
    'KH': 10,
    }
spades_dict = {
    'AS': 1 or 11,
    '2S': 2,
    '3S': 3,
    '4S': 4,
    '5S': 5,
    '6S': 6,
    '7S': 7,
    '8S': 8, 
    '9S': 9,
    '10S': 10,
    'JS': 10,
    'QS': 10,
    'KS': 10,
}
clubs_dict = {
    'AC': 1 or 11,
    '2C': 2,
    '3C': 3,
    '4C': 4,
    '5C': 5,
    '6C': 6,
    '7C': 7,
    '8C': 8, 
    '9C': 9,
    '10C': 10,
    'JC': 10,
    'QC': 10,
    'KC': 10,
}
diamonds_dict = {
    'AD': 1 or 11,
    '2D': 2,
    '3D': 3,
    '4D': 4,
    '5D': 5,
    '6D': 6,
    '7D': 7,
    '8D': 8, 
    '9D': 9,
    '10D': 10,
    'JD': 10,
    'QD': 10,
    'KD': 10,
}

hearts = hearts_dict
spades = spades_dict
clubs = clubs_dict
diamonds = diamonds_dict

DECK.append(hearts)
DECK.append(spades)
DECK.append(clubs)
DECK.append(diamonds)

class GameTable():
    DECK = [hearts, spades, clubs, diamonds]

    def __init__(self):
        random.shuffle(GameTable.DECK)
        self.deck = GameTable.DECK
        self.player_card= 0
        self.dealer_card= 0
        self.player_score = 0
        self.dealer_score = 0
        self.players_cards = []
        self.dealers_cards = []


    def deal_player(self):
        while len(self.players_cards) < 3:
            card = random.choice(self.deck)
            entry_list = list(card.items())
            self.player_card = random.choice(entry_list)
            self.players_cards.append(self.player_card)
            entry_list.remove(self.player_card)
            if len(self.players_cards) == 2:
                break
        player_score = sum(self.players_cards[0][1])
        print(player_score)   
        player_table = []
        for self.player_card in enumerate(self.players_cards, start =0):
            player_table.append(f"[ {self.player_card} ]") 
        return player_table 
    
    def deal_dealer(self):
        while len(self.dealer_card) < 3:
            card = random.choice(self.deck)
            entry_list = list(card.items())
            self.dealer_card = random.choice(entry_list)
            self.dealers_cards.append(self.dealer_card)
            self.deck.remove(self.dealer_card)
            if len(self.dealers_cards) == 2:
                break
        dealer_score = sum(self.dealers_cards)
        print(f"[ ] + [{self.dealer_card}]")
        print(dealer_score)

class Dealer(GameTable):
    def __init__(self, name= "Dealer", card =0):
        self.name = "Dealer"
        self.card = 0

        super.__init__(self)

    def hit(self):
        if self.dealer_score <= 16:
            card = random.choice(self.deck)
            entry_list = list(card.items())
            self.cards = random.choice(entry_list)
            self.dealers_cards.append(self.dealer_card)
            self.deck.remove(self.dealer_card)
            new_score = sum(self.dealers_cards)
            new_score = self.dealer_score
            print(self.dealer_score)

        elif self.dealer_score >= 17:
            self.stand()
            print(self.dealer_score)

        elif self.dealer_score == 21:
            print("Dealer has 21.  Dealer wins. ")
            self.stand()

        elif self.dealer_score > 21:
            print("Dealer Busts.  Player wins. ")
            self.stand()

    def stand(self):
        dealer_table = []
        for self.dealer_card in enumerate(self.dealers_cards, start =0):
            dealer_table.append(f"[ {self.dealer_card} ]") 
        return dealer_table 


class Player(GameTable):
    def __init__(self, name= "Player", card =0):
        self.name = "Player"
        self.card = 0
        super().__init__(self)

    def hit(self):
        r = input("Would you like to 'hit'? Yes or No? \n")
        clear_screen()
        if r.lower() == "yes":
            card = random.choice(self.deck)
            entry_list = list(card.items())
            self.player_card = random.choice(entry_list)
            self.players_cards.append(self.player_card)
            self.deck.remove(self.player_card)
            self.player_score = sum(self.players_cards)
            print(self.player_score)
            if self.player_score == 21:
                print("Congratulations you win! ")
                self.stand()
            elif self.player_score > 21:
                print("Sorry, you Bust.  Game over, dealer wins.")
                self.stand()
            elif self.player_score <= 21:
                self.hit()
        else:
            self.stand()

    def stand(self):
        player_table = []
        for self.player_card in enumerate(self.players_cards, start =0):
            player_table.append(f"[ {self.player_card} ]") 
        return player_table 
       

class UI():
    game = GameTable()

    @classmethod
    def play_game(cls):
        print("""
        Let's play Black Jack!
        Object of the game: Beat the dealer by getting count as close to 21 as possible, without going over 21.
        
        Ace (A) is worth 1 or 11, face cards (J,Q,K) are worth 10, and the rest of the cards equal their pip value.
        The Player receives 2 cards, both face up, from the dealer.  The dealer will also receive 2 cards, with one of them facing down.
        The dealer must "Hit" if their count <= 16. And, they must "Stand" if their count >= 17.

        ########### TERMINOLOGY ########### 
        "Hit" will give the player/dealer another card, one at a time.
        "Stand" will not produce another card.  
        "Bust" the count of either the player or dealers hand exceeds the value of 21. The opponent wins.
           

        """)
        input("Press enter to continue...")
        while True:
            clear_screen()
            print("""
    ===============================================================
    |                       Black Jack                            |
    ===============================================================            
            """)
            cls.game.deal_player()
            cls.game.deal_dealer()
            cls.player.hit()
            cls.dealer.hit()
            if player_score > dealer_score and player_score <= 21:
                print("Player's count is closer to 21.  Player wins! ")
            else:
                response = input("Game over.  Would you like to play again? Type: Yes or No. ")
                if response.lower() == 'yes': 
                    cls.play_game()
                else:
                    print("Thank you for playing! ")
                    break

    #Driver Code
    @classmethod
    def main(cls):
        cls.play_game()
   
  
UI.main()


                
        


          

       



   



    




