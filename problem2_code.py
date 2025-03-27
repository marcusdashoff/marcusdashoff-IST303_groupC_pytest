# THIS IS DUMMY CODE TO TEST OUR TEST FILE! 

def determine_board_state(input_list):
    if input_list == [[0, 1, 2], [0, 1, 0],[2, 1, 0]]:
        return 1
    
    if input_list == [[0, 2, 1], [0, 2, 0],[1, 2, 0]]:
        return 2
    
    return 0