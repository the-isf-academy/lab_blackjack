from blackjack import Blackjack
from view import TerminalView

game = Blackjack()
game_running = True

view = TerminalView()
view.welcome()
view.deal_starting_cards()


while game_running:
    view.beginning_turn(game.current_player_index)

    if game.get_player_type() == 'player':

        view.view_player_cards(game.current_player_hand())

        action = view.menu("\n[move]",["hit","stand"])


        if action == 'hit':
            game.hit(game.current_player_index)
          
            if game.check_bust(game.current_player_index):
                view.bust(game.current_player_index)
                game.increment_player_num()
            

        elif action == 'stand':
            game.increment_player_num()

    elif game.get_player_type() == 'computer':
        game.computer_turn()
        game.increment_player_num()
    
    if game.check_end() == False:
        game_running = False

winner = game.get_winner()
view.winner(game.get_winner())











