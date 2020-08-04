from collections import deque
a = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
a = [1102,34915192,34915192,7,4,7,99,0]
a = [3,8,1005,8,330,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,29,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,51,1006,0,78,2,107,9,10,1006,0,87,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,82,2,1103,5,10,1,101,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,112,1006,0,23,1006,0,20,1,2,11,10,1,1007,12,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,148,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,170,2,101,12,10,2,5,7,10,1,102,10,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,205,1,1004,10,10,2,6,13,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,235,2,102,4,10,1006,0,16,1006,0,84,1006,0,96,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,269,1006,0,49,2,1003,6,10,2,1104,14,10,1006,0,66,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,305,2,1,11,10,101,1,9,9,1007,9,1020,10,1005,10,15,99,109,652,104,0,104,1,21102,838479487744,1,1,21102,1,347,0,1106,0,451,21101,666567967640,0,1,21101,358,0,0,1106,0,451,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,28994219048,0,1,21102,405,1,0,1105,1,451,21102,3375459559,1,1,21101,0,416,0,1106,0,451,3,10,104,0,104,0,3,10,104,0,104,0,21102,838433665892,1,1,21102,1,439,0,1106,0,451,21102,988669698816,1,1,21102,450,1,0,1105,1,451,99,109,2,21201,-1,0,1,21102,1,40,2,21101,482,0,3,21102,472,1,0,1105,1,515,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,477,478,493,4,0,1001,477,1,477,108,4,477,10,1006,10,509,1101,0,0,477,109,-2,2105,1,0,0,109,4,1201,-1,0,514,1207,-3,0,10,1006,10,532,21101,0,0,-3,22102,1,-3,1,21201,-2,0,2,21102,1,1,3,21101,551,0,0,1106,0,556,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,579,2207,-4,-2,10,1006,10,579,21201,-4,0,-4,1105,1,647,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,0,598,0,1106,0,556,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,617,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,639,22102,1,-1,1,21101,0,639,0,106,0,514,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
# a = [109,19, 204,-34]
a = deque(a)
a = a + deque([0] * 10000)
i = 0
# a[1985] = 6666
inBuffer = [0]
relativeBase = 0
outBuffer = deque([])
lookingDirection = 0
paintCount = 0
seenPoses = set()
whitePoses = set()
blackPoses = set()
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
        print("running opcode 3")
        if instruct[-3] == '0':
            # a[a[i + 1]] = inBuffer[-1]
            if (yPos, xPos) not in whitePoses:
                a[a[i + 1]] = 0
            else:
                a[a[i + 1]] = 1
            # a[a[i + 1]] = inBuffer.pop()

        elif instruct[-3] == '1':
            # a[i + 1] = inBuffer[-1]
            # a[i + 1] = inBuffer.pop()
            if (y, x) not in whitePoses:
                a[i + 1] = 0
            else:
                a[i + 1] = 1
        elif instruct[-3] == '2':
            print("trying to access", a[i + 1] +relativeBase)
            # a[a[i + 1] +relativeBase] = inBuffer.pop()
            if (y, x) not in whitePoses:
                a[a[i + 1]+relativeBase] = 0
            else: 
                a[a[i + 1]+relativeBase] = 1
        i += 2
    elif opcode == 4:
        print("running code 4")
        if instruct[-3] == '0':
            print(a[a[i + 1]])
            outBuffer.append(a[a[i + 1]])
        elif instruct[-3] == '1':
            print(a[i + 1])
            outBuffer.append(a[i + 1])
        elif instruct[-3] == '2':
            print(a[a[i + 1]+relativeBase])
            outBuffer.append(a[a[i + 1]+relativeBase])
        if len(outBuffer) % 2 == 0:
            if outBuffer[-2] == 0:
                blackPoses.add((yPos, xPos))
                if (yPos, xPos) in whitePoses:
                    whitePoses.remove((yPos, xPos))
            else:
                whitePoses.add((yPos, xPos))
                if (yPos, xPos) in blackPoses:
                    blackPoses.remove((yPos, xPos))
            seenPoses.add((yPos, xPos))
            if outBuffer[-1] == 0:
                lookingDirection = (lookingDirection - 1) % 4
            else:
                lookingDirection = (lookingDirection + 1) % 4

            if lookingDirection == 0:
                yPos -= 1
            elif lookingDirection == 1:
                xPos += 1
            elif lookingDirection == 2:
                yPos += 1
            elif lookingDirection == 3:
                xPos -= 1



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



        print("new relativeBase", relativeBase)
        i += 2
    # print(outBuffer)

    # print('i', i)
    print(len(whitePoses))
    print(len(blackPoses))
    print(len(seenPoses))

# print(a)
print(outBuffer)
print(len(whitePoses))
print(len(blackPoses))
print(len(seenPoses))
b = deque([deque(["_"]*50) for i in range(50)])

for i in blackPoses:
    b[i[0]][i[1]] = " "
for i in whitePoses:
    b[i[0]][i[1]] = "O"
for i in b:
    for j in i:
        print(j, end='')
    print()