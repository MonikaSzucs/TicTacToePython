''' Tic Tac Toe Game
    By Monika Szucs
    Started: April 26, 2020
'''

#matrix
game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
       
#print top row numbers
print("   a  b  c")

#loop through matrix and count left column
for count, row in enumerate(game):
    print(count, row)
