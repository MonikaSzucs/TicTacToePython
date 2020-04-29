''' Tic Tac Toe Game
    By Monika Szucs
    Started: April 26, 2020
'''

import itertools

'''
player_choice = itertools.cycle([1,2])

for i in range(10):
    print(next(player_choice))
'''
#iterable: a thing we can iterate over
#iterator: a special object with next() method

#iterable... with a for loop or something... it has a end
#x = [1, 2, 3, 4]

#iterator (goes on forever)... also iterable
#n = itertools.cycle(x)

#for i in n:
#    print(i)

#y = iter(x)

#for i in y:
#    print(i)

#matrix
game = [[1, 0, 1],
       [2, 1, 2],
       [2, 0, 1]]
'''
You can win:
horizontally
vertically
diagonally
'''

cols = list(reversed(range(len(game))))
rows = range(len(game))


def win(current_game):
    # Horizontal
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally (-)")

    #diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/)!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (\\)")

    #vertical
    for col in range(len(game)):
        check = []

        for row in game:
            print(row[0])
            check.append(row[col])

        if row.count(check[0]) == len(row) and row[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|)")


#function
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    #print top row numbers
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player

        #loop through matrix
        for count, row in enumerate(game_map):
            print(count, row)
        #raise can also be added before return
        return game_map
    except IndexError as e:
            print("Error: make sure you input row/column as 0 1 or 2?", e)
    except Exception as e:
        print("Something went very wrong!", e)


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)


'''
this are some other things you can add but not needed right now
    else:

    finally:
'''
#
#print(game)
#game = game_board(game, just_display=True)
#game = game_board(game_board, player=1, row=3, column=1)
#print(game)

'''

open up cmd
type in cd ot nevigate to folder
the type: python game.py

'''
