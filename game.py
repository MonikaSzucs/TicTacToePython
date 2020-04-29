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

'''
You can win:
horizontally
vertically
diagonally
'''

#cols = list(reversed(range(len(game))))
#rows = range(len(game))


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (-)")
            return True

    #diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    #vertical
    for col in range(len(game)):
        check = []

        for row in game:
            print(row[0])
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically (|)")
            return True

    return False


#function
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    #print top row numbers
    try:
        if game_map[row][column] != 0:
            print("This position is occupide! Choose another")
            return game_map, False
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player

        #loop through matrix
        for count, row in enumerate(game_map):
            print(count, row)
        #raise can also be added before return
        return game_map, True
    except IndexError as e:
            print("Error: make sure you input row/column as 0 1 or 2?", e)
            return game_map, False
    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Goodbye")
                play = False
            else:
                print("Not a valid answer so see you later.")
                play = False



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
