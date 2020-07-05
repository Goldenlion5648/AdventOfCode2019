RAW = '''.#..#
.....
#####
....#
...##'''
# with open()
board = list(map(list, RAW.split('\n')))
print(board)
asteroidMapCount = dict()
visible = dict()
maxSeen = -100
pos = 0
lookingPos = (0,0)
dummy = 1000

positionMap = dict()
for y in range(len(board)):
# for y in range(2, 3):
    for x in range(len(board[0])):
    # for x in range(1, 2):
        if board[y][x] == '#':
            seen = []
            positions = []
            for i in range(10):
                for j in range(10):
                    if i == 0 and j == 0:
                        continue
                    try:
                        if 0 <= y + i < len(board) and 0 <= x+j <len(board[0]):
                            if board[y+i][x+j] == '#':
                                if j != 0:
                                    if (i,j) not in positions: 
                                        seen.append((i/j, 2))
                                        positions.append((i, j))
                                else:
                                    if (dummy,  False) not in positions:
                                        seen.append((dummy, 2))
                                        positions.append((dummy,  2))
                                # board[y+i][x+j] = 'A'
                        if 0 <= y + i < len(board) and 0 <= x-j <len(board[0]):
                            if board[y+i][x-j] == '#':
                                if j != 0:
                                    if (i,-j) not in positions: 
                                        seen.append((i/-j, 0))
                                        positions.append((i, -j))
                                else:
                                    if (dummy,  0) not in positions:
                                        seen.append((dummy, 0))
                                        positions.append((dummy,  0))
                                # board[y+i][x-j] = 'A'
                        if 0 <= y - i < len(board) and 0 <= x+j <len(board[0]):
                            if board[y-i][x+j] == '#':
                                if j != 0:
                                    if (-i,j) not in positions: 
                                        seen.append((-i/j, 1))
                                        positions.append((-i, j))
                                else:
                                    if (dummy,  1) not in positions:
                                        seen.append((dummy, 1))
                                        positions.append((dummy,  1))
                                # board[y-i][x+j] = 'A'
                        if 0 <= y - i < len(board) and 0 <= x-j <len(board[0]):
                            if board[y-i][x-j] == '#':
                                if j != 0:
                                    if (-i,-j) not in positions: 
                                        seen.append((-i/-j, 3))
                                        positions.append((-i, -j))
                                else:
                                    if (dummy,  3) not in positions:
                                        seen.append((dummy, 3))
                                        positions.append((dummy,  3))
                                # board[y-i][x-j] = 'A'
                    except Exception as ex:
                        print(ex)
                        continue
            seen = set(seen)
            print(seen)
            positions = set(positions)
            positionMap[(x,y)] = positions
            asteroidMapCount[(x,y)] = len(seen)
            visible[(x,y)] = seen
            if len(seen) > maxSeen:
                maxSeen = len(seen)
                pos = (x, y)
            # maxSeen = max(maxSeen, len(seen))
# print(pos)
# print(set(pos))
print(maxSeen)
print(asteroidMapCount)
# for i in asteroidMapCount[(1,2)]:

# print(visible[(1,2)])
# print(pos)
# print(positionMap[(1,2)])
# for i in board:
#     print("".join(i))
# for i in positionMap[(1,2)]:
#     print(i)
#     if i[0] != dummy:
#         board[2 + i[0]][1 + i[1]] = 'A'
# print()
# for i in board:
#     print("".join(i))