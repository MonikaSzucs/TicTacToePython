''' Tic Tac Toe Game
    By Monika Szucs
    Started: April 26, 2020
'''

#matrix
game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


#function
def game_board(player=0, row=0, column=0, just_display=False):
    #print top row numbers
    print("   a  b  c")
    if not just_display:
        game[row][column] = player

    #loop through matrix
    for count, row in enumerate(game):
        print(count, row)


game_board(just_display=True)
game_board(player=1, row=1, column=1)
