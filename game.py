''' Tic Tac Toe Game
    By Monika Szucs
    Started: April 26, 2020
'''

#matrix
game = [[2, 0, 0],
       [0, 2, 0],
       [0, 0, 2]]
'''
You can win:
horizontally
vertically
diagonally
'''

cols = list(reversed(range(len(game))))
rows = range(len(game))

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

print(diags)


if game[0][0] == game[1][1] == game[2][2]:
    print("winner")



if game[2][0] == game[1][1] == game[0][2]:
    print("winner")


'''
columns = [0, 1, 2]


for col in range(len(game)):
    check = []

    for row in game:
        print(row[0])
        check.append(row[col])

    if row.count(check[0]) == len(row) and row[0] != 0:
        print("Winner")

def win(current_game):
    for row in game:
        print(row)

        all_match = True
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner")


win(game)
'''

#function
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    #print top row numbers
    try:
        print("   a  b  c")
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

'''
this are some other things you can add but not needed right now
    else:

    finally:
'''

print(game)
game = game_board(game, just_display=True)
game = game_board(game_board, player=1, row=3, column=1)
print(game)

'''

open up cmd
type in cd ot nevigate to folder
the type: python game.py

'''
