RAW = '''.#..#
.....
#####
....#
...##'''

RAW = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''
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
                                        seen.append((i/j))
                                        positions.append((i, j))
                                else:
                                    if (dummy, 2) not in positions:
                                        seen.append((dummy))
                                        positions.append((dummy))
                                # board[y+i][x+j] = 'A'
                        if 0 <= y + i < len(board) and 0 <= x-j <len(board[0]):
                            if board[y+i][x-j] == '#':
                                if j != 0:
                                    if (i,-j) not in positions: 
                                        seen.append((i/-j))
                                        positions.append((i, -j))
                                else:
                                    if (dummy, 0) not in positions:
                                        seen.append((dummy))
                                        positions.append((dummy))
                                # board[y+i][x-j] = 'A'
                        if 0 <= y - i < len(board) and 0 <= x+j <len(board[0]):
                            if board[y-i][x+j] == '#':
                                if j != 0:
                                    if (-i,j) not in positions: 
                                        seen.append((-i/j))
                                        positions.append((-i, j))
                                else:
                                    if (dummy, 1) not in positions:
                                        seen.append((dummy))
                                        positions.append((dummy))
                                # board[y-i][x+j] = 'A'
                        if 0 <= y - i < len(board) and 0 <= x-j <len(board[0]):
                            if board[y-i][x-j] == '#':
                                if j != 0:
                                    if (-i,-j) not in positions: 
                                        seen.append((-i/-j))
                                        positions.append((-i, -j))
                                else:
                                    if (dummy, 2) not in positions:
                                        seen.append((dummy))
                                        positions.append((dummy))
                                # board[y-i][x-j] = 'A'
                    except Exception as ex:
                        print(ex)
                        continue
            # seen = set(seen)
            # print(seen)
            # positions = set(positions)
            positionMap[(x,y)] = positions
            asteroidMapCount[(x,y)] = len(positions)
            visible[(x,y)] = seen
            if len(positions) > maxSeen:
                maxSeen = len(positions)
                pos = (x, y)
            # maxSeen = max(maxSeen, len(seen))
# print(pos)
# print(set(pos))
# print(maxSeen)
print(asteroidMapCount)
# for i in asteroidMapCount[(1,2)]:

# print(visible[(1,2)])
# print(pos)
# print(positionMap[(1,2)])
givenAnswerPos = pos
print(pos)
answerPositionsYX = []
for i in positionMap[givenAnswerPos]:
    if i == 1000:
        continue
    slopes = [x[2] for x in answerPositionsYX]
    cur = i[0]/i[1]

    if cur not in slopes:
        answerPositionsYX.append((i[0], i[1], cur))
    else:
        potentials = []
        for k in answerPositionsYX:
            if k[2] == cur:
                potentials.append(k)
        works = True
        for k in potentials:
            if not((k[0] >= 0) != (i[0] >= 0) or (k[1] >= 0) != (i[1] >= 0)):
                works = False
                break
        if works:
            answerPositionsYX.append((i[0], i[1], cur))
        else:
            print('not found', answerPositionsYX[slopes.index(cur)])
board[givenAnswerPos[1]][givenAnswerPos[0]] = 'S'
# for i in board:
#     print("".join(i))
for j in answerPositionsYX:
    i = (j[0], j[1])
    # print(i)
    if i != dummy:
        board[givenAnswerPos[1] + i[0]][givenAnswerPos[0] + i[1]] = 'A'
print()
for i in board:
    print("".join(i))
print(len(answerPositionsYX))