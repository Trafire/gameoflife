import math
import tkinter

class Cell:
    def __init__(self,row_length, index, state):
        self.x = index % row_length
        self.y = index // row_length
        self.index = index
        self.state = state[index]

    def  __str__(self):
        return str(self.state)
        

    def update(self,state, canvas):
        self.state = state[self.index]
        canvas.itemconfigure(self.cell, fill = self.state_colour())
        
        
    def state_colour(self):
        if self.state == '0':
            return 'black'
        else:
            return 'red'
    def draw_cells(self,canvas):
        self.cell = canvas.create_rectangle(self.x *10, 10+self.y *10, 10+self.x *10, self.y *10, fill = self.state_colour())

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
    new_state = ''
    for index in range(row_length**2):
        neighbors = count_neighbors(index,state,row_length)
        cell = life(neighbors,state[index])
        new_state = new_state + cell
    return new_state

def init_draw(cell_obj, canvas):
    for e in cell_obj:
        e.draw_cells(canvas)

def draw(canvas, state, row_length, cell_obj):
    
    new_state = cycle(state, row_length)
    for e in cell_obj:
        e.update(new_state,canvas)

    

    return new_state


    
state = '0000000000000000000000000000000000000011000001100000000011000110000000100101010100100001110110110111000001010101010100000001110001110000000000000000000000000111000111000000010101010101000001110110110111000010010101010010000000110001100000000011000001100000000000000000000000000000000000000'
row_length = int(math.sqrt(len(state)))

cell_obj = [Cell(row_length,x,state) for x in range(row_length**2)]
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=500, height=500)
init_draw(cell_obj, canvas)
canvas.pack()
state = draw(canvas, state, row_length,cell_obj)

