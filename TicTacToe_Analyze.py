#Author: Bogdan Trigubov
#Date: Nov, 15, 2024
#Description: Program that check the results of a txt tic-tac-toe gand prints the results. 
import sys

def state_from_file(filename):
    """ Return the game state stored in the given file as a length-9 list.
    Precondition: file is a txt file with the data arranged in the following format:
        x|x|x
        x|o|o
        o| |x
    """
    with open(filename) as file_:
        file_list = []
        final_list = []
        string = ""
        for line in file_: #creates list with all the lines as strings
            file_list = file_list+[line]
        for string in file_list:
            string = string.replace("\n","|").lower().split("|")
            string = string[0:3]
            #del string[3]# index 3 is unnecessary and wrong
            final_list = final_list + string
            final_list = final_list[0:9]
        state = final_list
    return state #game state 

def get_row(state, i):
    """ Return a length-3 list containing the ith row of the game state.
    Rows are 0-indexed, so the rows are numbered 0, 1, and 2. 
    Precondition: state is a list, i is an int.""" 
    if i == 0:
        row = state[0:3]
    if i == 1:
        row = state[3:6]
    if i == 2:
        row = state[6:9]
    return row

def get_col(state, i):
    """ Return a length-3 list containing the ith column of the game state.
    Columns are 0-indexed, so the columns are numbered 0, 1, and 2. 
    Precondition: state is a list, i is an int."""
    column = []
    if i == 0:
        column_str = state[0]+state[3]+state[6]
        for char in column_str:
             column.append(char)
    if i == 1:
        column_str = state[1]+state[4]+state[7]
        for char in column_str:
             column.append(char)        
    if i == 2:
        column_str = state[2]+state[5]+state[8]
        for char in column_str:
             column.append(char)
    return column

def get_diag(state, i):
    """ Return a length-3 list containing the ith diagonal of the game state.
      diagonal 0 is the one going from the top-left to the bottom-right
      diagonal 1 is the one going from the bottom-left to the top-right. 
      Precondition: state is a list, i is an int."""
    diagonal = []
    if i == 0:
        diagonal_str = state[0]+state[4]+state[8]
        for char in diagonal_str:
             diagonal.append(char)
    if i == 1:
        diagonal_str = state[2]+state[4]+state[6]
        for char in diagonal_str:
             diagonal.append(char)    
    return diagonal
   
def state_str(state):
    """ Return a string representation of the game state that matches the
    one read from the file, except with moves displayed as upper-case X and O
    Precondition: state is a list"""
    string1 = ""
    string2 = ""
    string3 = ""
    list1=[]
    list2=[]
    list3=[]
    row_1_list = state[0:3]
    row_2_list = state[3:6]
    row_3_list = state[6:9]
    for item in row_1_list: #Takes state and adds "|" to it, removes the last one, and adds a "\n" at the end, then converts it to string for each row. 
        list1 += [item] + ["|"]
    del list1[5]
    list1 = list1+["\n"]
    for item in list1:
        string1 += item
    #BUFFER
    for item in row_2_list:
        list2 += [item] + ["|"]
    del list2[5]
    list2 = list2+["\n"]
    for item in list2:
        string2 += item
    #BUFFER
    for item in row_3_list:
        list3 += [item] + ["|"]
    del list3[5]
    list3 = list3+["\n"]
    del list3[5]
    for item in list3:
        string3 += item
    final_string = string1+string2+string3
    final_string = final_string.upper()
    return final_string
def count_moves(state):
    """ Count the number of moves by either player that have been made so far
    in the game. 
    precondition: state is a list """
    state_string = ""
    for item in state:
        state_string += item
    no_turns = state_string.count(" ")
    turns = 9 - no_turns
    return turns
def analyze(state):
    """ Analyze the game state to determine which player (if any) has won, and
    where. Returns a length-3 tuple containing:
        - the winning player ("x" or "o", as a string)
        - the winning direction ("row", "column", or "diagonal")
        - the winning location (0, 1, or 2, defined as in the get_* functions.)
    precondition: state is a list"""
    #DIAGONAL OPERATIONS 
    diag_0_list = get_diag(state,0)
    diag_1_list = get_diag(state,1)
    d = "nowin"
    if diag_0_list ==["x","x","x"]: 
        d = ("x","diagonal",0)
    if diag_0_list ==["o","o","o"]: 
        d = ["o","diagonal",0]
    if diag_1_list ==["x","x","x"]: 
        d = ["x","diagonal",1]
    if diag_1_list ==["o","o","o"]: 
        d = ["o","diagonal",1]
    
    #COLUMN OPERATIONS
    c = "nowin"
    for column in range(0,3):
        col_list = get_col(state,column)
        if col_list == ["x","x","x"]:
            c = ["x","column",column]
        if col_list == ["o","o","o"]:
            c = ("o","column",column)
        
    #ROW OPERATIONS
    r = "nowin"
    for row in range(0,3):
        row_list = get_row(state,row)
        if row_list == ["x","x","x"]:
            r = ("x","row",row)
        if row_list == ["o","o","o"]:
            r = ("x","row",row)

    if d=="nowin" and c=="nowin" and r =="nowin":
        return None
    if d != "nowin":
        process = d
    if c != "nowin":
        process = c
    if r != "nowin":
        process = r    
    return process
if __name__ == "__main__":
    tuple = analyze(state_from_file("tictactoe_games.txt"))
    moves = count_moves(state_from_file("tictactoe_games.txt"))
    if tuple == None:
        print("After ", moves, " moves nobody has won.", sep="")
    else:
        winner = tuple[0]
        how = tuple[1]
        where = tuple[2]
        print("After ", moves," moves player ", winner, " has won on ", how, " ", where, sep="")