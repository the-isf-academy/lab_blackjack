from deck import Deck

class Blackjack:
    def __init__(self):
        self.deck = Deck('cards.csv')

        self.hands = {
            0: {
                'type': 'player',
                'hand': [],
                'bust': False
            },      
            1: {
                'type': 'player',
                'hand': [],
                'bust': False
            },
            2: {
                'type': 'computer',
                'hand': [],
                'bust': False
            }, 
        }


        self.current_player_index = 0

        self.deal_initial_cards()

    def deal_n_cards(self, n):
        # deal n cards from deck

        cards = []
        for i in range(n):
            card = self.deck.get_top_card()
            cards.append(card)

        return cards

    def deal_initial_cards(self):
        # deals 2 cards to each player

        for player, details in self.hands.items():
            for card in self.deal_n_cards(2):
                details['hand'].append(card)

      
    def hit(self, player_index):
        # deals 1 card to specific player

        for card in self.deal_n_cards(1):
            self.hands[player_index]['hand'].append(card)
       
    def get_hand_value(self, player_index):
        # returns total integer value of player cards

        value = 0
        ace_count = 0
        
        for card in self.hands[player_index]['hand']:
            if card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                value += 11
                ace_count += 1
            else:
                value += int(card.rank)
        
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        
        return value
    
    def check_bust(self, player_index):
        # check if player has cards valued over 21

        if self.get_hand_value(player_index) > 21:
            self.hands[player_index]['bust'] = True
            return True
        return False
    
    def get_player_type(self):
        # returns type of player 

        return self.hands[self.current_player_index]['type']

    def current_player_hand(self):
        # returns the current Player hand.
     
        return self.hands[self.current_player_index]['hand']
    
    def increment_player_num(self):
        # increment current player index

        self.current_player_index = self.current_player_index + 1

    def computer_turn(self):
        # hits computer for 1 card

        self.hit(2)

    def get_winner(self):
        # returns the winner based on the highest value

        winner_player_index = None
        highest_value = 0

        for player_index, details in self.hands.items():
            if not details['bust']:
                current_val = self.get_hand_value(player_index)
                if winner_player_index is None or current_val > highest_value:
                    highest_value = current_val
                    winner_player_index = player_index

        if winner_player_index is None:
            return "No winner, all players busted."

        if self.hands[winner_player_index]['type'] == 'computer':
            return 'Computer'
        else:
            return f"Player {winner_player_index}"
    
    def check_end(self):
        # check no players are left

        return self.current_player_index < len(self.hands)

if __name__ == "__main__":
    blackjack = Blackjack()

    # 💻 experiment with the attributes and methods
    # ensure you understand how the game works

    blackjack.deal_initial_cards()
    for card in blackjack.current_player_hand():
        print(card)
 




