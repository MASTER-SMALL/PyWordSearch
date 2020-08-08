import tkinter as tk
import random
import string

grid_size = 10

grid = [ [ '_' for _ in range(grid_size) ] for _ in range(grid_size) ]

orientations = [ 'leftright', 'updown', 'diagonalup', 'diagonaldown' ]

class Button(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs, font=("Courier", 14))

class LabelSmall(tk.Label):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs, font=("Courier", 14))
        
class Label(tk.Label):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs, font=("Courier", 44))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        def mainFunc():
            handle = open('dictionary.txt')
            words = handle.readlines()
            handle.close()
            words = [ random.choice(words).upper().strip() \
            for _ in range(5) ]
            print ("The words are:")
            print(words)
            def listWords():
                word_length = len(words)
                LabelSmall(self, text="The words are:").grid(row=0, column=grid_size+1)
                for i in range(word_length):
                    LabelSmall(self, text=words[i]).grid(row=i+1, column=grid_size+1)
            Button(self, text="Reshuffle Grid", command=mainFunc).grid(row=grid_size, column=grid_size+1)
            for word in words:
                word_length = len(word)
                
                placed = False
                while not placed:
                    orientation = random.choice(orientations)

                    if orientation == 'leftright':
                        step_x = 1
                        step_y = 0
                    if orientation == 'updown':
                        step_x = 0
                        step_y = 1
                    if orientation == 'diagonalup':
                        step_x = 1
                        step_y = -1
                    if orientation == 'diagonaldown':
                        step_x = 1
                        step_y = 1

                    x_position = random.randrange(grid_size)
                    y_position = random.randrange(grid_size)

                    ending_x = x_position + word_length*step_x
                    ending_y = y_position + word_length*step_y

                    if ending_x < 0 or ending_x >= grid_size: continue
                    if ending_y < 0 or ending_y >= grid_size: continue

                    failed = False


                    for i in range(word_length):
                        character = word[i]

                        new_position_x = x_position + i*step_x
                        new_position_y = y_position + i*step_y

                        character_at_new_position = grid[new_position_x][new_position_y]
                        if character_at_new_position != '_':
                            if character_at_new_position == character:
                                continue
                            else:
                                failed = True
                                print("failed")


                    if failed:
                        print('randomizing spot')
                        for row in range(grid_size):
                            for column in range(grid_size):
                                if ( grid[row][column] == '_' ):
                                    txt = random.SystemRandom().choice(string.ascii_uppercase)
                                    Label(self, text=txt).grid(row=row, column=column)
                        continue
                    else:
                        for i in range(word_length):
                            character = word[i]

                            new_position_x = x_position + i*step_x
                            new_position_y = y_position + i*step_y

                            grid[new_position_x][new_position_y] = character
                            for row in range(grid_size):
                                for column in range (grid_size):
                                    if ( grid[row][column] == grid[new_position_x][new_position_y] ):
                                        grid[row][column] = grid[new_position_x][new_position_y]
                                        Label(self, text=character).grid(row=row, column=column)
                        placed = True
            listWords()
        mainFunc()


if __name__ == '__main__':
    App().mainloop()