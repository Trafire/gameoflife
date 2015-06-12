############1. import modules
import math
import tkinter 
############2a. def classes
class Board:
    def __init__(self, state,row_length):
        self.state = state
        self.row_length = row_length
        self.cells = [Cells(self,x) for x in range(row_length**2)]



    def advance_state(self):
        self.state = cycle(self.state, self.row_length)
    def get_state(self):
        return self.state
    def get_row_length(self):
        return int(self.row_length)
    def get_cell(self,index):
        return self.state[index]
    def update_cells(self):
        for cell in self.cells:
            cell.update_cell()
            
        
    

class Cells:
    def __init__(self, board, index):
        self.x = index % board.get_row_length()
        self.y = index // board.get_row_length()
        self.index = index
        self.board = board
        self.state = board.get_state()[index]
        self.colour = self.state_colour()
        self.cell = canvas.create_rectangle(self.x *10, 10+self.y *10, 10+self.x *10, self.y *10, fill = self.colour)

    def  __str__(self):
        return str(self.state)

    def state_colour(self):

        if self.state == '0':
            return 'black'
        else:
            return 'red'
    def update_cell(self):
        self.state = self.board.get_cell(self.index)
        self.colour = self.state_colour()
        self.colouring()

    def colouring(self):
        canvas.itemconfigure(self.cell, fill = self.colour)
  
    
    
        
        
        

############2b. set Global Variables

state = '0000000000000000000000000000000000000011000001100000000011000110000000100101010100100001110110110111000001010101010100000001110001110000000000000000000000000111000111000000010101010101000001110110110111000010010101010010000000110001100000000011000001100000000000000000000000000000000000000'
#state = '0001000000000111000000000010000000000011000001100000000011000110000000100001010100100001110110110111000001010101010100000001110001110000000000000010000000000111000111000000010101010101001001110110110111000010010101010010000000110001100000000011000001100000000000000000000000000000000000000'



row_length = int(math.sqrt(len(state)))
cell_size = 10



############3. define helper functions
def life(neighbors, cell):
    '''(int, str) -> str
    neighbors is the number of neighbors a cell has, evals based on rules and
    returns, 1 or 0 depending on life or death
    >>> life(4,1)
    '0'
    >>> life(3,0)
    '1'
    >>> life(2,0)
    '0'
    '''
    
    if neighbors == 3:
        life = '1'
    elif neighbors == 2 and cell == '1':
        life = '1'
    else:
        life = '0'
    return life

def count_neighbors(index, state, row_length):
    ''' (int, str) -> int
    index is the position the cell is in the state, state is a string
    of 1 and 0s representing, living or dead.
    Returns the number of live cells adjacent or  diagnal to the cell
    '''
    neighbors = []

    left = index - 1
    right = index + 1
    top = index - row_length
    bottom = index + row_length
    
    upper_right = index - row_length + 1
    upper_left = index - row_length - 1
    lower_right = index + row_length + 1
    lower_left = index + row_length - 1

    left_side = False
    right_side = False

    if index % row_length != 0:
        left_side = True
        neighbors.append(int(state[left]))
        
    if index % row_length != row_length-1:
        right_side = True
        neighbors.append(int(state[right]))

    if index//row_length != 0:
        neighbors.append(int(state[top]))
        if left_side:
            neighbors.append(int(state[upper_left]))
        if right_side:
            neighbors.append(int(state[upper_right]))
    
    if index//row_length != row_length-1:
        neighbors.append(int(state[bottom]))
        if left_side:
            neighbors.append(int(state[lower_left]))
        if right_side:
            neighbors.append(int(state[lower_right]))

       
    return sum(neighbors)

def cycle(state, row_length):
    ''' (str, int) ->
    state is current game state, row_length is board dimension - returns updated board
    '''
    new_state = ''
    for index in range(row_length**2):
        neighbors = count_neighbors(index,state,row_length)
        cell = life(neighbors,state[index])
        new_state = new_state + cell
    return new_state


############4. Event Handlers

def tick(board):
    board.advance_state()
    board.update_cells()
    
    
    frame.after(500, tick, board)

############5. create frame & frame
frame = tkinter.Tk()
canvas = tkinter.Canvas(frame, width= row_length*cell_size, height=row_length*cell_size)

############6. register event handers
board = Board(state,row_length)


canvas.pack()
############7. initailize
tick(board)
