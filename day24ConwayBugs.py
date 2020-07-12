from copy import deepcopy
RAW = '''....#
#..#.
#..##
..#..
#....'''

RAW = '''####.
.##..
##.#.
###..
##..#'''

board = list(map(list, RAW.split('\n')))
temp = deepcopy(board)
time = 400
for j in temp:
    print(*j)
print()
seen = []
for i in range(time):
    for y in range(len(board)):
        for x in range(len(board[y])):
            count = 0
            if y > 0 and board[y-1][x] == '#':
                count += 1
                # print('y1')
            if x > 0 and board[y][x-1] == '#':
                count += 1
                # print('x1')
            if y < len(board) -1  and board[y+1][x] == '#':
                count += 1
                # print('y2')
            if x < len(board) -1  and board[y][x+1] == '#':
                count += 1
                # print('x2')
            if count != 1:
                temp[y][x] = '.'
            # print(y, x, 'count', count)

            if (count == 1 or count == 2) and board[y][x] =='.':
                temp[y][x] = '#'
    for j in temp:
        print(*j, sep='')
    print()
    board = deepcopy(temp)
    if temp not in seen:
        seen.append(deepcopy(temp))
    else:
        print('broke out')
        print(i)
        break

bio = 0
mult = 1
for q in range(len(temp)):
    for w in range(len(temp[0])):
        
        if temp[q][w] == '#':
            bio += mult
        mult *= 2
print(bio)