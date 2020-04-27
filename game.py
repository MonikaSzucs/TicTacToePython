''' Tic Tac Toe Game
    By Monika Szucs
    Started: April 26, 2020
'''

#matrix
game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


#function
def game_board():
    #loop through matrix and count left column
    for count, row in enumerate(game):
        if (count == 1):
            game[1][0] = 1
        print(count, row)


#print top row numbers
print("   a  b  c")

game_board()
