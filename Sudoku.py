board=[[".", ".", "4", ".", ".", ".", "6", "3", "."],
       [".", ".", ".", ".", ".", ".", ".", ".", "."],
       ["5", ".", ".", ".", ".", ".", ".", "9", "."],
       [".", ".", ".", "5", "6", ".", ".", ".", "."],
       ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
       [".", ".", ".", "7", ".", ".", ".", ".", "."],
       [".", ".", ".", "5", ".", ".", ".", ".", "."],
       [".", ".", ".", ".", ".", ".", ".", ".", "."],
       [".", ".", ".", ".", ".", ".", ".", ".", "."]]
my_dict = {}
count = 0
#my_dict[]=[]
for k in range(27):
    my_dict[k]=[]

for i in range(9):
    my_dict[i]=[]
    # Filling rows
    for j in range(9):
        if (board[i][j]).isnumeric():
            my_dict[i].append(int(board[i][j]))
            cunt=9+j
            my_dict[cunt].append(int(board[i][j]))


for i in range(9):
    for j in range(9):
        if (board[i][j]).isnumeric():
            count = 18
            count=count+(int(j/3)+(3*int(i/3)))
            my_dict[count].append(int(board[i][j]))



print(my_dict)