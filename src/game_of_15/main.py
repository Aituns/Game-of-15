import numpy as np

def main():
    board_state = [0,1,0,0,0,0,0,0,0]
    new_board_state = [0,1,0,0,1,0,0,0,0]
    print(np.setdiff1d(board_state, new_board_state))
    

if __name__ == "__main__":
    main()