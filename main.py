import os
from random import randint
from game_board import TicTacToe
# Starting board
tic_tac_toe = TicTacToe()
board_cells = tic_tac_toe.starting_cells()
header_and_board = tic_tac_toe.display_board(board_cells=board_cells)

def print_board():
    os.system("cls")
    header_and_board = tic_tac_toe.display_board(board_cells=board_cells)
    print(header_and_board)

# Who Goes first
who_goes_first = 1
current_game = True
play_again = True

print_board()

# Player choice for X and O

player_choice = input("\nWelcome! Player 1, please pick 'X' or 'O': ").upper()
if player_choice == "O":
    p1_symbol = "O"
    p2_symbol = "X"
else:
    p1_symbol = "X"
    p2_symbol = "O"

# First turn
if who_goes_first % 2 == 1:
    input(f"\nPlayer 1 symbol: {p1_symbol}\nPlayer 2 symbol: {p2_symbol} \n\nPlayer 1 goes first! Press any key to start...")
else:
    input(f"\nPlayer 1 symbol: {p1_symbol}\nPlayer 2 symbol: {p2_symbol} \n\nPlayer 2 goes first! Press any key to start...")

### REPLAYABILITY ###
while play_again == True:
    
    if current_game == False:
        keep_playing = input("\nWould you like to play again? Yes or No: ").lower()
        # GAME RESET
        if keep_playing[0] == "y":
            board_cells = tic_tac_toe.starting_cells()
            tic_tac_toe.turns = 0
            who_goes_first += 1
            current_game = True
            if who_goes_first % 2 == 1:
                input(f"\nPlayer 1 symbol: {p1_symbol}\nPlayer 2 symbol: {p2_symbol} \n\nPlayer 1 goes first! Press any key to start...")
            else:
                input(f"\nPlayer 1 symbol: {p1_symbol}\nPlayer 2 symbol: {p2_symbol} \n\nPlayer 2 goes first! Press any key to start...")
        # END GAME
        else:
            os.system("clear")
            print(f"Thank you for playing!\n_____________________\nFINAL SCORE\n- - - - - - - - - - -\nPlayer 1 games won: {tic_tac_toe.p1_wins}\nPlayer 2 games won: {tic_tac_toe.p2_wins}")
            play_again = False 

    else:
        ### SINGLE GAME ###
        print_board()
        while current_game == True: 
            player1_win_check = tic_tac_toe.winning_combinations(player="Player 1", symbol=p1_symbol, board_cells=board_cells)
            player2_win_check = tic_tac_toe.winning_combinations(player="Player 2", symbol=p2_symbol, board_cells=board_cells)
            
            ### PLAYER 1 GOES FIRST ###
            if who_goes_first % 2 == 1:
                # Tie check
                if tic_tac_toe.turns == 9:
                    print_board()
                    print(f"The game has ended in a tie...")
                    current_game=False
                # Player 1 turn
                else:
                    player1=tic_tac_toe.player_placement(player="Player 1", symbol=p1_symbol, board_cells=board_cells)
                    print_board()
                    player1_win_check = tic_tac_toe.winning_combinations(player="Player 1", symbol=p1_symbol, board_cells=board_cells)
                    # Player 1 win check
                    if player1_win_check == True:
                        tic_tac_toe.p1_wins += 1
                        print_board()
                        print(f"Player 1 has won the game!")
                        current_game=False
                    
                    # PLAYER 2 TURN
                    elif player1_win_check != True:
                        # Tie check
                        if tic_tac_toe.turns == 9:
                            print_board()
                            print(f"The game has ended in a tie...")
                            current_game=False
                        # Player 2 turn
                        else:
                            player2=tic_tac_toe.player_placement(player="Player 2", symbol=p2_symbol, board_cells=board_cells)
                            print_board()
                            player2_win_check = tic_tac_toe.winning_combinations(player="Player 2", symbol=p2_symbol, board_cells=board_cells)
                            # Player 2 win check
                            if player2_win_check == True:
                                tic_tac_toe.p2_wins += 1
                                print_board()
                                print(f"Player 2 has won the game!")
                                current_game=False

            ### PLAYER 2 GOES FIRST ###
            else:
                # Tie check
                if tic_tac_toe.turns == 9:
                    print_board()
                    print(f"The game has ended in a tie...")
                    current_game=False
                # Player 2 turn
                else:
                    player2=tic_tac_toe.player_placement(player="Player 2", symbol=p2_symbol, board_cells=board_cells)
                    print_board()
                    player2_win_check = tic_tac_toe.winning_combinations(player="Player 2", symbol=p2_symbol, board_cells=board_cells)
                    # Player 2 win check
                    if player2_win_check == True: 
                        tic_tac_toe.p2_wins += 1
                        print_board()
                        print(f"Player 2 has won the game!")
                        current_game=False
                    
                    ### PLAYER 1 TURN ###
                    elif player2_win_check != True:
                        # Tie check
                        if tic_tac_toe.turns == 9:
                            print_board()
                            print(f"The game has ended in a tie...")
                            current_game=False
                        # Player 1 turn
                        else:
                            player1=tic_tac_toe.player_placement(player="Player 1", symbol=p1_symbol, board_cells=board_cells)
                            print_board()
                            player1_win_check = tic_tac_toe.winning_combinations(player="Player 1", symbol=p1_symbol, board_cells=board_cells)
                            # Player 1 Win check
                            if player1_win_check == True:
                                tic_tac_toe.p1_wins += 1
                                print_board()
                                print(f"Player 1 has won the game!")
                                current_game=False