import numpy as np

class Board:
    ROWS = 3
    COLUMNS = 3

    board_state = [0,0,0,0,0,0,0,0,0]

    def made_move(new_board_state):
        if (Board.board_state == new_board_state):
            return False
        else:
            return True
    
    def check_duplicate(new_board_state):
        dup = {x for x in new_board_state if new_board_state.count(x) > 1}
        if (len(dup) > 0):
            return False
        else:
            return True
        
    def check_out_of_turn(new_board_state):
        even_count = 0
        odd_count  = 0
        while(num < len(new_board_state)):
            # checking condition
            if new_board_state[num] % 2 == 0 and new_board_state[num] != 0:
                even_count += 1
            else:
                odd_count += 1
            num += 1

        if even_count + 1 > odd_count or odd_count +1 > even_count:
            return False
        else: 
            return True


    def playmove(new_board_state):
        if not Board.made_move(new_board_state):
            return "Error: No Move Made"
        if not Board.check_duplicate(new_board_state):
            return "Error: Duplicate Move"
        if not Board.check_out_of_turn(new_board_state):
            return "Error: Out of Turn"
        Board.board_state = new_board_state
        

        