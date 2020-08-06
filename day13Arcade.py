from collections import deque
def drawBoard(gameTiles):
    print("len of gameTiles", len(gameTiles))
    didMove = False
    maxX = max(gameTiles, key=lambda x:x[0])[0] + 2
    maxY = max(gameTiles, key=lambda x:x[1])[1] + 2
    # print(maxX)
    # print(maxY)
    board = deque([deque([" "]*(maxX)) for k in range(maxY)])
    for tile in gameTiles:
# print(tile)
        cur = 0
        if tile[2] == 0:
            cur = "."
        elif tile[2] == 1:
            cur = "#"
        elif tile[2] == 2:
            cur = "%"
        elif tile[2] == 3:
            cur = "|"
        elif tile[2] == 4:
            cur = "O"
        board[tile[1]][tile[0]] = cur
    board[paddleY][paddleX] = 'T'
    board[ballPosY][ballPosX] = 'O'
    print("ball pos", ballPosX, ballPosY)
    # print("ball pos", ballPosX, ballPosY)
    for k in range(len(board)):
        # for j in range(len(board[k])):
        print("".join(board[k]), end='')
        print()

        

a = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
a = [1102,34915192,34915192,7,4,7,99,0]
a = [2,380,379,385,1008,2235,561969,381,1005,381,12,99,109,2236,1102,1,0,383,1101,0,0,382,21002,382,1,1,21001,383,0,2,21102,1,37,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,38,381,1005,381,22,1001,383,1,383,1007,383,21,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1106,0,161,107,1,392,381,1006,381,161,1101,-1,0,384,1105,1,119,1007,392,36,381,1006,381,161,1102,1,1,384,21001,392,0,1,21102,19,1,2,21102,1,0,3,21101,138,0,0,1105,1,549,1,392,384,392,20102,1,392,1,21102,1,19,2,21102,3,1,3,21101,161,0,0,1105,1,549,1101,0,0,384,20001,388,390,1,20101,0,389,2,21101,180,0,0,1105,1,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21001,389,0,2,21102,1,205,0,1105,1,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21101,0,228,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,20102,1,388,1,20001,389,391,2,21102,253,1,0,1105,1,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21102,1,279,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,1,304,0,1106,0,393,1002,390,-1,390,1002,391,-1,391,1101,0,1,384,1005,384,161,21001,388,0,1,21002,389,1,2,21101,0,0,3,21102,1,338,0,1106,0,549,1,388,390,388,1,389,391,389,21001,388,0,1,21001,389,0,2,21102,4,1,3,21102,365,1,0,1105,1,549,1007,389,20,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,253,17,16,1,1,19,109,3,21201,-2,0,1,21201,-1,0,2,21102,1,0,3,21102,1,414,0,1106,0,549,21202,-2,1,1,21201,-1,0,2,21102,429,1,0,1105,1,601,1201,1,0,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2105,1,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22101,0,-3,-7,109,-8,2105,1,0,109,4,1202,-2,38,566,201,-3,566,566,101,639,566,566,2102,1,-1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,38,594,201,-2,594,594,101,639,594,594,20101,0,0,-2,109,-3,2106,0,0,109,3,22102,21,-2,1,22201,1,-1,1,21101,401,0,2,21101,380,0,3,21101,798,0,4,21101,630,0,0,1106,0,456,21201,1,1437,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,0,2,0,0,0,2,2,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,2,2,2,0,0,0,2,2,2,2,0,1,1,0,2,0,2,2,2,2,2,2,0,2,0,0,0,2,0,2,2,2,2,2,0,2,0,0,2,2,2,2,2,0,0,2,0,0,0,1,1,0,2,2,2,0,2,2,2,2,0,0,2,2,2,2,0,2,2,2,2,0,2,2,0,0,2,0,0,0,2,0,0,2,2,0,0,1,1,0,0,0,0,2,2,0,0,2,0,2,0,2,0,0,2,2,2,2,0,2,2,0,0,2,0,0,2,2,2,2,2,0,0,0,0,1,1,0,2,2,2,2,2,2,2,0,2,2,2,0,2,2,0,0,0,2,2,0,0,2,0,2,2,0,0,2,2,2,0,2,2,2,0,1,1,0,2,0,0,2,2,2,0,0,0,0,0,0,0,0,2,2,0,0,2,2,0,2,2,0,2,2,2,0,0,0,2,0,0,0,0,1,1,0,2,2,0,2,2,0,2,2,2,0,0,2,0,2,2,0,0,0,2,0,2,0,2,2,2,0,0,2,2,0,2,2,2,2,0,1,1,0,0,0,0,2,2,2,0,2,2,2,0,2,2,2,0,0,2,2,0,0,2,2,2,2,0,2,2,0,0,2,0,0,2,0,0,1,1,0,2,2,2,2,2,2,2,2,0,2,0,0,0,0,2,2,0,0,0,0,0,0,0,2,2,2,0,2,0,2,2,2,0,2,0,1,1,0,2,0,0,2,2,0,2,2,0,2,2,0,2,2,2,0,0,2,2,2,0,0,2,0,2,2,2,0,2,2,0,0,0,0,0,1,1,0,2,2,2,0,2,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,0,0,0,2,0,2,0,2,2,2,2,2,2,0,0,1,1,0,2,0,2,0,0,0,2,2,0,2,0,0,2,2,0,0,0,0,2,2,0,2,2,2,0,0,2,0,2,0,2,0,2,0,0,1,1,0,0,2,2,2,0,0,2,0,0,2,0,2,2,0,2,0,2,2,0,0,0,0,0,0,2,0,0,2,2,0,2,2,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,91,80,96,50,92,18,83,16,45,62,94,81,49,93,61,86,79,95,45,22,82,45,49,34,21,37,74,22,4,82,40,45,36,71,27,98,54,89,17,44,39,27,24,8,2,85,70,13,10,63,7,34,64,58,98,36,7,53,97,23,11,7,16,21,10,69,75,6,73,97,48,49,89,37,79,1,34,94,71,6,23,32,53,44,35,95,67,82,49,25,55,86,94,32,58,33,33,14,23,9,98,44,1,49,28,93,19,65,88,61,72,54,7,91,78,95,32,91,98,57,54,67,1,15,45,47,1,88,90,59,4,83,90,92,8,21,1,58,8,75,39,94,43,19,67,77,36,52,17,54,19,48,45,86,16,35,85,19,59,32,73,14,11,74,89,71,39,69,96,61,77,84,93,45,70,16,85,40,62,12,30,98,38,53,50,54,87,1,70,53,84,60,10,70,83,93,33,24,95,11,96,48,98,24,66,89,51,4,66,42,57,55,23,17,77,70,3,6,93,24,63,89,19,39,37,93,92,72,32,59,4,90,40,15,16,62,59,9,15,40,2,94,86,32,29,36,71,3,28,14,76,79,45,51,32,96,96,50,54,82,84,41,2,33,90,28,6,85,45,63,86,58,85,85,91,18,23,28,47,67,60,70,53,19,73,40,6,61,38,65,15,3,76,86,18,65,80,63,36,34,56,1,35,90,47,62,25,15,76,53,6,30,10,77,78,51,86,61,50,66,58,92,98,73,93,82,88,91,23,72,35,87,19,53,52,26,68,81,46,76,4,55,32,47,51,14,52,12,31,97,2,53,41,97,1,74,60,40,31,9,33,67,7,9,81,98,62,81,17,35,54,80,52,40,14,27,45,57,54,8,29,78,18,35,5,86,63,17,38,44,98,48,25,9,42,58,1,9,67,36,68,9,27,63,55,7,54,43,62,69,40,6,30,10,79,86,44,59,96,22,94,62,86,47,63,9,31,72,82,78,69,41,83,35,97,15,42,19,3,21,44,56,24,23,48,62,73,20,3,43,95,67,85,30,47,41,93,93,43,41,83,62,18,15,48,51,9,85,46,24,38,34,86,67,40,15,56,48,84,96,79,48,80,73,83,12,33,40,6,94,62,31,82,12,88,81,56,73,83,45,24,61,78,45,39,21,70,80,36,94,56,48,10,53,76,81,34,24,96,37,22,45,85,64,17,95,91,18,95,38,50,20,93,24,17,82,81,42,51,32,41,35,78,64,14,92,76,64,28,57,9,53,34,18,6,19,38,90,42,9,32,83,76,61,6,56,70,59,86,55,18,88,33,59,18,76,1,36,85,43,65,30,44,30,98,37,54,19,71,21,72,30,91,72,9,66,16,11,31,47,18,71,44,9,68,85,92,76,92,50,31,12,87,77,89,7,25,21,68,48,23,1,48,21,79,66,38,16,26,86,46,74,24,68,94,43,78,73,72,5,73,8,60,95,76,40,62,57,56,59,22,82,32,43,22,83,85,13,5,12,37,31,39,25,43,46,75,5,84,52,36,25,80,65,10,4,71,11,9,68,50,38,97,33,93,83,45,60,86,8,56,55,24,73,90,24,30,96,68,70,16,56,30,61,13,38,76,21,27,66,70,82,87,45,39,51,57,62,9,47,44,37,82,49,41,17,13,68,42,49,87,52,37,6,12,74,5,37,43,79,25,85,18,39,56,37,67,34,82,71,91,54,40,16,10,51,7,22,83,31,72,46,74,29,13,40,57,85,94,40,33,10,25,9,61,87,30,44,78,23,41,35,36,30,23,96,27,10,25,32,55,25,15,70,39,90,38,8,561969]
# a = [109,19, 204,-34]
a = deque(a)
a = a + deque([0] * 1000)
i = 0
# a[1985] = 6666
didMove = False
# inBuffer = [0] 
# inBuffer = [-1,-1,-1,-1,1,1, 0, 0, 1,1,1,1,1]
# inBuffer = [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,-1,-1,-1,-1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,
# 0,00,0,0,0,0] + [0]*56 + [1]*4 + [0]*10 + [-1]*8 + [0] * 20 + [1]*7 + [0] * 30 + [-1] + [0] * 43 + [-1]*5 + [0]*10 + [1] * 3 + [0]*50
inBuffer = []
relativeBase = 0
outBuffer = deque([])
lookingDirection = 0
paintCount = 0
seenPoses = set()
whitePoses = set()
blackPoses = set()
gameTiles = deque()
blockCount = 0
scoreTracker = [0]
paddleX = 0
paddleY = 0
ballPosX = 0
ballPosY = 0
ballMovingDirection = 1
bouncingDirection = 1
moveInstruct = 0
appendedInputCount = 0
# isCurColor =
xPos = 0
yPos = 0
whitePoses.add((yPos, xPos))
# boardDim = 500
# board = deque(deque([0] * boardDim)) 
while i < len(a):
    opcode = a[i] % 100
    # print('opcode', opcode)
    # print("inBuffer", inBuffer)
    instruct = '0' * 5 + str(a[i])
    if len(gameTiles) > 793:
        # print(instruct)
        # print("opcode", opcode)
        # print(i)
        pass



    if opcode == 1:
        l = 0
        r= 0
        if instruct[-5] == '0':
            if instruct[-3] == '0':
                l = a[a[i+1]] 
            elif instruct[-3] == '1':
                l = a[i+1]
            elif instruct[-3] == '2':
                l = a[a[i+1]+relativeBase]
            if instruct[-4] == '0':
                r = a[a[i+2]] 
            elif instruct[-4] == '1':
                r = a[i+2]
            elif instruct[-4] == '2':
                r = a[a[i+2]+relativeBase]

            a[a[i + 3]] = l + r
        elif instruct[-5] == '1':
            if instruct[-3] == '0':
                l = a[a[i+1]] 
            elif instruct[-3] == '1':
                l = a[i+1]
            elif instruct[-3] == '2':
                l = a[a[i+1]+relativeBase]
            if instruct[-4] == '0':
                r = a[a[i+2]] 
            elif instruct[-4] == '1':
                r = a[i+2]
            elif instruct[-4] == '2':
                r = a[a[i+2]+relativeBase]

            a[i + 3] = l + r 
        elif instruct[-5] == '2':
            if instruct[-3] == '0':
                l = a[a[i+1]] 
            elif instruct[-3] == '1':
                l = a[i+1]
            elif instruct[-3] == '2':
                l = a[a[i+1]+relativeBase]
            if instruct[-4] == '0':
                r = a[a[i+2]] 
            elif instruct[-4] == '1':
                r = a[i+2]
            elif instruct[-4] == '2':
                r = a[a[i+2]+relativeBase]

            a[a[i + 3]+relativeBase] = l + r
        
        # elif instruct[-5] == '1':
        #     a[i+3] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) + (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
        # elif instruct[-5] == '2':
        #     a[a[i + 3] + relativeBase] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) + (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
        

        i += 4
    elif opcode == 2:
        l = 0
        r= 0
        if instruct[-5] == '0':
            if instruct[-3] == '0':
                l = a[a[i+1]] 
            elif instruct[-3] == '1':
                l = a[i+1]
            elif instruct[-3] == '2':
                l = a[a[i+1]+relativeBase]
            if instruct[-4] == '0':
                r = a[a[i+2]] 
            elif instruct[-4] == '1':
                r = a[i+2]
            elif instruct[-4] == '2':
                r = a[a[i+2]+relativeBase]

            a[a[i + 3]] = l * r
        elif instruct[-5] == '1':
            if instruct[-3] == '0':
                l = a[a[i+1]] 
            elif instruct[-3] == '1':
                l = a[i+1]
            elif instruct[-3] == '2':
                l = a[a[i+1]+relativeBase]
            if instruct[-4] == '0':
                r = a[a[i+2]] 
            elif instruct[-4] == '1':
                r = a[i+2]
            elif instruct[-4] == '2':
                r = a[a[i+2]+relativeBase]

            a[i + 3] = l * r 
        elif instruct[-5] == '2':
            if instruct[-3] == '0':
                l = a[a[i+1]] 
            elif instruct[-3] == '1':
                l = a[i+1]
            elif instruct[-3] == '2':
                l = a[a[i+1]+relativeBase]
            if instruct[-4] == '0':
                r = a[a[i+2]] 
            elif instruct[-4] == '1':
                r = a[i+2]
            elif instruct[-4] == '2':
                r = a[a[i+2]+relativeBase]

            a[a[i + 3]+relativeBase] = l * r

        # if instruct[-5] == '0':
        #     a[a[i + 3]] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) * (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
        # elif instruct[-5] == '1':
        #     a[i + 3] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) * (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
        # elif instruct[-5] == '2':
        #     a[a[i + 3] +relativeBase] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) * (a[a[i+2]] if instruct[-4] == '0' else a[i+2])

        i += 4
    elif opcode == 3:
        # print("running opcode 3")
        if scoreTracker[-1] > 4800:
            drawBoard(gameTiles)
        # moveInstruct = ballMovingDirection
        # moveInstruct = int(input("Enter movement >"))
        moveInstruct = inBuffer.pop(0)

        # if paddleX < ballPosX:
        #     moveInstruct = 1
        # elif paddleX > ballPosY:
        #     moveInstruct = -1
        # print("scores", scoreTracker)
        # paddleY -= moveInstruct
        # if inBuffer[-1] == -1:
        #     paddleY += 1
        #     paddleY -= 1
        if instruct[-3] == '0':
            # a[a[i + 1]] = inBuffer[-1]
            # if (yPos, xPos) not in whitePoses:
            #     a[a[i + 1]] = 0
            # else:
            #     a[a[i + 1]] = 1
            # a[a[i + 1]] = inBuffer.pop()
            a[a[i + 1]] = moveInstruct

        elif instruct[-3] == '1':
            # a[i + 1] = inBuffer[-1]
            # a[i + 1] = inBuffer.pop()
            a[i + 1] = moveInstruct
            # if (y, x) not in whitePoses:
            #     a[i + 1] = 0
            # else:
            #     a[i + 1] = 1
        elif instruct[-3] == '2':
            # print("trying to access", a[i + 1] +relativeBase)
            # a[a[i + 1] +relativeBase] = inBuffer.pop()
            a[a[i + 1] +relativeBase] = moveInstruct
            # if (y, x) not in whitePoses:
            #     a[a[i + 1]+relativeBase] = 0
            # else: 
            #     a[a[i + 1]+relativeBase] = 1
        else:
            print("something went wrong with input")
        didMove = True
        # print(inBuffer)
        # print("moved")
        i += 2
    elif opcode == 4:
        # print("running code 4")
        if instruct[-3] == '0':
            # print(a[a[i + 1]])
            outBuffer.append(a[a[i + 1]])
        elif instruct[-3] == '1':
            # print(a[i + 1])
            outBuffer.append(a[i + 1])
        elif instruct[-3] == '2':
            # print(a[a[i + 1]+relativeBase])
            outBuffer.append(a[a[i + 1]+relativeBase])
        if len(outBuffer) % 3 == 0:
            # print(outBuffer)
            # print(outBuffer[-3:])
            # if outBuffer[-1] == 4:
            #     if (outBuffer[-3], outBuffer[-2], 2) in gameTiles:
            #         gameTiles.remove((outBuffer[-3], outBuffer[-2], 2))
            #         print("removed")
                # gameTiles = [i for i in gameTiles if i[2] != 4]
            if outBuffer[-1] == 3:
                paddleY = outBuffer[-2]
                paddleX = outBuffer[-3]
            elif outBuffer[-3] == -1 and outBuffer[-2] == 0:

                print("score", scoreTracker[-1]) 
                scoreTracker.append(outBuffer[-1])
            else:
                if outBuffer[-1] != 4:
                    potentialBlockAtPos = (outBuffer[-3], outBuffer[-2], 2)
                    if potentialBlockAtPos in gameTiles:
                        gameTiles.remove(potentialBlockAtPos)
                    gameTiles.append((outBuffer[-3], outBuffer[-2], outBuffer[-1]))
                else:
                    if ballPosX < outBuffer[-3]:
                        bouncingDirection = 1
                    elif ballPosX > outBuffer[-3]:
                        bouncingDirection = -1
                    else:
                        bouncingDirection = 0

                    ballPosX = outBuffer[-3]
                    ballPosY = outBuffer[-2]
                    if len(inBuffer) < 1:
                        

                        if ballPosX + (bouncingDirection*(paddleY-ballPosY) -1) > paddleX:
                            inBuffer.append(1)
                        elif ballPosX + (bouncingDirection*(paddleY-ballPosY) + 1) < paddleX:
                            inBuffer.append(-1)
                        else:
                            inBuffer.append(0)
                        appendedInputCount += 1
                        print("len of inBuffer", len(inBuffer))

                        # print("appended input", appendedInputCount)

                    # if bouncingDirection == -1:
                    #     if ballPosX < paddleX:
                    #         moveInstruct = -1
                    #     elif ballPosX > outBuffer[-3]:
                    #         moveInstruct = 1
                    #     else:
                    #         moveInstruct = 0
                    # else:
                    #     if ballPosX + (bouncingDirection*(paddleY-ballPosY))-2 > paddleX:
                    #         moveInstruct = -1
                    #     elif ballPosX + (bouncingDirection*(paddleY-ballPosY))+2 < paddleX:
                    #         moveInstruct = 1
                    #     else:
                    #         moveInstruct = 0
                    if ballPosX == paddleX and ballPosY + 1 == paddleY:
                        moveInstruct = bouncingDirection
                    # print("new ball pos", ballPosX, ballPosY)
                    # print("paddle pos", paddleX, paddleY)
            if outBuffer[-1] == 2:
                blockCount += 1
            # if outBuffer[-2] == 0:
                # blackPoses.add((yPos, xPos))
                # if (yPos, xPos) in whitePoses:
                #     whitePoses.remove((yPos, xPos))
            # else:
            #     whitePoses.add((yPos, xPos))
            #     if (yPos, xPos) in blackPoses:
            #         blackPoses.remove((yPos, xPos))
            # seenPoses.add((yPos, xPos))
            # print("did output", outBuffer)
            outBuffer = deque()
            # if outBuffer[-1] == 0:
            #     lookingDirection = (lookingDirection - 1) % 4
            # else:
            #     lookingDirection = (lookingDirection + 1) % 4

            # if lookingDirection == 0:
            #     yPos -= 1
            # elif lookingDirection == 1:
            #     xPos += 1
            # elif lookingDirection == 2:
            #     yPos += 1
            # elif lookingDirection == 3:
            #     xPos -= 1



        i += 2
    elif opcode == 5:
        if instruct[-3] == '0':
            if a[a[i+1]] != 0:
                if instruct[-4] == '0':
                    i = a[a[i+2]] 
                elif instruct[-4] == '1':
                    i = a[i+2]
                elif instruct[-4] == '2':
                    i = a[a[i+2]+relativeBase] 
            else:
                i += 3
        elif instruct[-3] == '1':
            if a[i+1] != 0:
                if instruct[-4] == '0':
                    i = a[a[i+2]] 
                elif instruct[-4] == '1':
                    i = a[i+2]
                elif instruct[-4] == '2':
                    i = a[a[i+2]+relativeBase]
            else:
                i += 3
        elif instruct[-3] == '2':
            if a[a[i+1]+relativeBase] != 0:
                if instruct[-4] == '0':
                    i = a[a[i+2]] 
                elif instruct[-4] == '1':
                    i = a[i+2]
                elif instruct[-4] == '2':
                    i = a[a[i+2]+relativeBase]
            else:
                i += 3
    elif opcode == 6:
        if instruct[-3] == '0':
            if a[a[i+1]] == 0:
                if instruct[-4] == '0':
                    i = a[a[i+2]] 
                elif instruct[-4] == '1':
                    i = a[i+2]
                elif instruct[-4] == '2':
                    i = a[a[i+2]+relativeBase] 
            else:
                i += 3
        elif instruct[-3] == '1':
            if a[i+1] == 0:
                if instruct[-4] == '0':
                    i = a[a[i+2]] 
                elif instruct[-4] == '1':
                    i = a[i+2]
                elif instruct[-4] == '2':
                    i = a[a[i+2]+relativeBase] 
            else:
                i += 3
        elif instruct[-3] == '2':
            if a[a[i+1]+relativeBase] == 0:
                if instruct[-4] == '0':
                    i = a[a[i+2]] 
                elif instruct[-4] == '1':
                    i = a[i+2]
                elif instruct[-4] == '2':
                    i = a[a[i+2]+relativeBase] 
            else:
                i += 3
    elif opcode == 7:
        if instruct[-3] == '0':
            if instruct[-4] == '0':
                if a[a[i + 1]] < a[a[i + 2]]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '1':
                if a[a[i + 1]] < a[i + 2]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '2':
                if a[a[i + 1]] < a[a[i + 2]+relativeBase]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
        elif instruct[-3] == '1':
            if instruct[-4] == '0':
                if a[i + 1] < a[a[i + 2]]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '1':
                if a[i + 1] < a[i + 2]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '2':
                if a[i + 1] < a[a[i + 2]+relativeBase]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
        elif instruct[-3] == '2':
            if instruct[-4] == '0':
                if a[a[i + 1]+relativeBase] < a[a[i + 2]]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '1':
                if a[a[i + 1]+relativeBase] < a[i + 2]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '2':
                if a[a[i + 1]+relativeBase] < a[a[i + 2]+relativeBase]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
        i += 4
    elif opcode == 8:
        if instruct[-3] == '0':
            if instruct[-4] == '0':
                if a[a[i + 1]] == a[a[i + 2]]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '1':
                if a[a[i + 1]] == a[i + 2]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '2':
                if a[a[i + 1]] == a[a[i + 2]+relativeBase]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
        elif instruct[-3] == '1':
            if instruct[-4] == '0':
                if a[i + 1] == a[a[i + 2]]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '1':
                if a[i + 1] == a[i + 2]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '2':
                if a[i + 1] == a[a[i + 2]+relativeBase]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
        elif instruct[-3] == '2':
            if instruct[-4] == '0':
                if a[a[i + 1]+relativeBase] == a[a[i + 2]]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '1':
                if a[a[i + 1]+relativeBase] == a[i + 2]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
            elif instruct[-4] == '2':
                if a[a[i + 1]+relativeBase] == a[a[i + 2]+relativeBase]:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 1
                    elif instruct[-5] == '1':
                        a[i+3] = 1
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 1
                else:
                    if instruct[-5] == '0':
                        a[a[i+3]] = 0
                    elif instruct[-5] == '1':
                        a[i+3] = 0
                    elif instruct[-5] == '2':
                        a[a[i+3]+relativeBase] = 0
        i += 4
    elif opcode == 99:
        break
    elif opcode == 9:
        # print("old relativeBase", relativeBase)
        # print(a[i])
        if instruct[-3] == '0':
            relativeBase += a[a[i+1]]
        elif instruct[-3] == '1':
            relativeBase += a[i+1]
        elif instruct[-3] == '2':
            relativeBase += a[a[i+1]+relativeBase]


        # print("new relativeBase", relativeBase)
        i += 2
    # print(outBuffer)
    if len(gameTiles) > 795:
        # print(outBuffer)
        pass
    # if didMove == True:
    #     drawBoard(gameTiles)
    #     didMove = False


    # print('i', i)
    # print(len(whitePoses))
    # print(len(blackPoses))
    # print(len(seenPoses))

# print(a)
# print(outBuffer)
# print(blockCount)
print("final score", scoreTracker[-5:])
drawBoard(gameTiles)
# maxX = max(gameTiles, key=lambda x:x[0])[0] + 2
# maxY = max(gameTiles, key=lambda x:x[1])[1] + 2
# print(maxX)
# print(maxY)
# board = deque([deque([" "]*maxY) for i in range(maxX)])
# for tile in gameTiles:
#     # print(tile)
#     cur = 0
#     if tile[2] == 0:
#         cur = "."
#     elif tile[2] == 1:
#         cur = "#"
#     elif tile[2] == 2:
#         cur = "%"
#     elif tile[2] == 3:
#         cur = "|"
#     elif tile[2] == 3:
#         cur = "O"
#     board[tile[0]][tile[1]] = cur
# for k in range(len(board)):
#     for j in range(len(board[k])):
#         print(board[k][j], end='')
#     print()
#     # print("".join(i))
# # print(len(whitePoses))
# print(scoreTracker)
# # print(inBuffer)
# print(len(gameTiles))
# print(len(blackPoses))
# print(len(seenPoses))
# b = deque([deque(["_"]*50) for i in range(50)])

# for i in blackPoses:
#     b[i[0]][i[1]] = " "
# for i in whitePoses:
#     b[i[0]][i[1]] = "O"
# for i in b:
#     for j in i:
#         print(j, end='')
#     print()
