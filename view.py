# class for View
# =============================================================================

from InquirerPy import inquirer, get_style          # different menu package for windows compatibility

class TerminalView:
    """Handles input and output from a Game.
    You should switch into a different mode while reading this file: here, it's about
    the "skin" the game – like a user interface – whereas over in game.py it's about the
    algorithms and interactions.

    Most important point: The View has no idea what is going on in the game, it
    just give messages for particular events.
    """

    def menu(self,prompt, options):
        '''This function creates an interactive Terminal menu.'''

        choice = inquirer.select(
            message= prompt,
            choices= options,
            qmark="",
            style= get_style({ 
                "answer": "#438fa8",
                "pointer": "#438fa8"})
            ).execute()

        return choice

    
    def welcome(self):
        print("-"*51)
        print("-"*20, "Blackjack", "-"*20)
        print("-"*51,"\n")

    def view_player_cards(self,cards):
        print("\n Current hand:")
        for card in cards:
            print(card)

    def deal_starting_cards(self):
        print("\n... 🔀 Dealing Cards")

    def beginning_turn(self, player_index):
        print("_"*70)
        print(f"\n👤 {player_index}, it is your turn.")

    def winner(self, player_index):
        print(f"\n🥇 {player_index} won!")

    def computer_turn(self):
        print(f"\n🤖 computer took its turn")

    def bust(self, player_index):
        print(f"\n😢 {player_index} went bus!")



   
  