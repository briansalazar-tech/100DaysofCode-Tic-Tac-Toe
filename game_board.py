class TicTacToe:


    def __init__(self):
        # Game Board
        self.game_on = True
        self.turns = 0
        self.p1_wins = 0
        self.p2_wins = 0
        self.header = """
╔════╗          ╔════╗             ╔════╗        
║╔╗╔╗║          ║╔╗╔╗║             ║╔╗╔╗║        
╚╝║║╚╝╔╗╔══╗    ╚╝║║╚╝╔══╗ ╔══╗    ╚╝║║╚╝╔══╗╔══╗
  ║║  ╠╣║╔═╝      ║║  ╚ ╗║ ║╔═╝      ║║  ║╔╗║║╔╗║
 ╔╝╚╗ ║║║╚═╗     ╔╝╚╗ ║╚╝╚╗║╚═╗     ╔╝╚╗ ║╚╝║║║═╣
 ╚══╝ ╚╝╚══╝     ╚══╝ ╚═══╝╚══╝     ╚══╝ ╚══╝╚══╝
                                                                                                      
      \n"""


    def starting_cells(self):
        """Create a clean dictionary for board"""
        cells ={
            "top_left" : "-",
            "top_center" : "-",
            "top_right" : "-",
            "mid_left" : "-",
            "mid_center" : "-",
            "mid_right" : "-",
            "bot_left" : "-",
            "bot_center" : "-",
            "bot_right" : "-",
        } 
        return cells


    def display_board(self, board_cells):
        """Displays a board with header"""
        score = f"Player 1 wins: {self.p1_wins} - Player 2 wins: {self.p2_wins}\nBoard slots used: {self.turns}\n"
        display = self.header + f" -------------  Board Positions\n | {board_cells['top_left']} | {board_cells['top_center']} | {board_cells['top_right']} | - TL, TC, TR \n ------------- \n | {board_cells['mid_left']} | {board_cells['mid_center']} | {board_cells['mid_right']} | - ML, MC, MR \n ------------- \n | {board_cells['bot_left']} | {board_cells['bot_center']} | {board_cells['bot_right']} | - BL, BC, BR  \n ------------- \n" + score
        return display


    def player_placement(self, player, symbol, board_cells):
        """Player entries to update the board dictionary"""
        valid_entry = False
        while valid_entry == False:
            entry = input(f"{player} - {symbol}, pick a spot on the board: ").upper()
            if entry == "TL" and board_cells["top_left"] == "-":
                board_cells["top_left"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "TC" and board_cells["top_center"] == "-":
                board_cells["top_center"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "TR" and board_cells["top_right"] == "-":
                board_cells["top_right"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "ML" and board_cells["mid_left"] == "-":
                board_cells["mid_left"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "MC" and board_cells["mid_center"] == "-":
                board_cells["mid_center"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "MR" and board_cells["mid_right"] == "-":
                board_cells["mid_right"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "BL" and board_cells["bot_left"] == "-":
                board_cells["bot_left"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "BC" and board_cells["bot_center"] == "-":
                board_cells["bot_center"] = symbol
                valid_entry = True
                self.turns += 1
            elif entry == "BR" and board_cells["bot_right"] == "-":
                board_cells["bot_right"] = symbol
                valid_entry = True
                self.turns += 1
            else:
                print("That is not a valid entry.")
                self.turns += 0


    def winning_combinations(self, player, symbol, board_cells):
        """Winning combinations for the X Player."""
        # Player wins backslash
        if board_cells["top_left"] == symbol and board_cells["mid_center"] == symbol and  board_cells["bot_right"] == symbol:
            return True
        # Player wins frontslash
        if board_cells["top_right"] == symbol and board_cells["mid_center"] == symbol and  board_cells["bot_left"] == symbol:
            return True
        # Player wins top horizontal
        if board_cells["top_left"] == symbol and board_cells["top_center"] == symbol and  board_cells["top_right"] == symbol:
            return True
        # Player wins center horizontal
        if board_cells["mid_left"] == symbol and board_cells["mid_center"] == symbol and  board_cells["mid_right"] == symbol:
            return True
        # Player wins bottom horizontal
        if board_cells["bot_left"] == symbol and board_cells["bot_center"] == symbol and  board_cells["bot_right"] == symbol:
            return True
        # Player wins left portrait
        if board_cells["top_left"] == symbol and board_cells["mid_left"] == symbol and  board_cells["bot_left"] == symbol:
            return True
        # Player wins center portrait
        if board_cells["mid_left"] == symbol and board_cells["mid_center"] == symbol and  board_cells["mid_right"] == symbol:
            return True
        # Player wins right portrait
        if board_cells["top_right"] == symbol and board_cells["mid_right"] == symbol and  board_cells["bot_right"] == symbol:
            return True