perms = [[0, 1, 2, 3, 4], [0, 1, 2, 4, 3], [0, 1, 3, 2, 4], [0, 1, 3, 4, 2], [0, 1, 4, 2, 3], [0, 1, 4, 3, 2], [0, 2, 1, 3, 4], [0, 2, 1, 4, 3], [0, 2, 3, 1, 4], [0, 2, 3, 4, 1], [0, 2, 4, 1, 3], [0, 2, 4, 3, 1], [0, 3, 1, 2, 4], [0, 3, 1, 4, 2], [0, 3, 2, 1, 4], [0, 3, 2, 4, 1], [0, 3, 4, 1, 2], [0, 3, 4, 2, 1], [0, 4, 1, 2, 3], [0, 4, 1, 3, 2], [0, 4, 2, 1, 3], [0, 4, 2, 3, 1], [0, 4, 3, 1, 2], [0, 4, 3, 2, 1], [1, 0, 2, 3, 4], [1, 0, 2, 4, 3], [1, 0, 3, 2, 4], [1, 0, 3, 4, 2], [1, 0, 4, 2, 3], [1, 0, 4, 3, 2], [1, 2, 0, 3, 4], [1, 2, 0, 4, 3], [1, 2, 3, 0, 4], [1, 2, 3, 4, 0], [1, 2, 4, 0, 3], [1, 2, 4, 3, 0], [1, 3, 0, 2, 4], [1, 3, 0, 4, 2], [1, 3, 2, 0, 4], [1, 3, 2, 4, 0], [1, 3, 4, 0, 2], [1, 3, 4, 2, 0], [1, 4, 0, 2, 3], [1, 4, 0, 3, 2], [1, 4, 2, 0, 3], [1, 4, 2, 3, 0], [1, 4, 3, 0, 2], [1, 4, 3, 2, 0], [2, 0, 1, 3, 4], [2, 0, 1, 4, 3], [2, 0, 3, 1, 4], [2, 0, 3, 4, 1], [2, 0, 4, 1, 3], [2, 0, 4, 3, 1], [2, 1, 0, 3, 4], [2, 1, 0, 4, 3], [2, 1, 3, 0, 4], [2, 1, 3, 4, 0], [2, 1, 4, 0, 3], [2, 1, 4, 3, 0], [2, 3, 0, 1, 4], [2, 3, 0, 4, 1], [2, 3, 1, 0, 4], [2, 3, 1, 4, 0], [2, 3, 4, 0, 1], [2, 3, 4, 1, 0], [2, 4, 0, 1, 3], [2, 4, 0, 3, 1], [2, 4, 1, 0, 3], [2, 4, 1, 3, 0], [2, 4, 3, 0, 1], [2, 4, 3, 1, 0], [3, 0, 1, 2, 4], [3, 0, 1, 4, 2], [3, 0, 2, 1, 4], [3, 0, 2, 4, 1], [3, 0, 4, 1, 2], [3, 0, 4, 2, 1], [3, 1, 0, 2, 4], [3, 1, 0, 4, 2], [3, 1, 2, 0, 4], [3, 1, 2, 4, 0], [3, 1, 4, 0, 2], [3, 1, 4, 2, 0], [3, 2, 0, 1, 4], [3, 2, 0, 4, 1], [3, 2, 1, 0, 4], [3, 2, 1, 4, 0], [3, 2, 4, 0, 1], [3, 2, 4, 1, 0], [3, 4, 0, 1, 2], [3, 4, 0, 2, 1], [3, 4, 1, 0, 2], [3, 4, 1, 2, 0], [3, 4, 2, 0, 1], [3, 4, 2, 1, 0], [4, 0, 1, 2, 3], [4, 0, 1, 3, 2], [4, 0, 2, 1, 3], [4, 0, 2, 3, 1], [4, 0, 3, 1, 2], [4, 0, 3, 2, 1], [4, 1, 0, 2, 3], [4, 1, 0, 3, 2], [4, 1, 2, 0, 3], [4, 1, 2, 3, 0], [4, 1, 3, 0, 2], [4, 1, 3, 2, 0], [4, 2, 0, 1, 3], [4, 2, 0, 3, 1], [4, 2, 1, 0, 3], [4, 2, 1, 3, 0], [4, 2, 3, 0, 1], [4, 2, 3, 1, 0], [4, 3, 0, 1, 2], [4, 3, 0, 2, 1], [4, 3, 1, 0, 2], [4, 3, 1, 2, 0], [4, 3, 2, 0, 1], [4, 3, 2, 1, 0]]
# perms = list(map(list, perms))
# perms = [[1,0,4,3,2]]
highest = -10000
for combo in perms:
    comboPos = 0
    inBuffer = combo.copy()
    outBuffer = [0]
    while comboPos < 5:
        #given instruction input
        a = [3,8,1001,8,10,8,105,1,0,0,21,38,59,76,89,106,187,268,349,430,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,3,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99]
        i = 0

        while i < len(a):
            opcode = a[i] % 100
            # print('opcode', opcode)


            instruct = '0' * 5 + str(a[i])
            if opcode == 1:
                if instruct[-5] == '0':
                    a[a[i + 3]] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) + (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
                else:
                    a[i+3] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) + (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
                

                i += 4
            elif opcode == 2:
                if instruct[-5] == '0':
                    a[a[i + 3]] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) * (a[a[i+2]] if instruct[-4] == '0' else a[i+2])
                else:
                    a[i + 3] = (a[a[i+1]] if instruct[-3] == '0' else a[i+1]) * (a[a[i+2]] if instruct[-4] == '0' else a[i+2])

                i += 4
            elif opcode == 3:
                if instruct[-3] == '0':
                    # a[a[i + 1]] = inBuffer[-1]
                    # print('took in', inBuffer[comboPos])
                    a[a[i + 1]] = inBuffer[comboPos]
                    inBuffer[comboPos] = outBuffer[-1]
                else:
                    # a[i + 1] = inBuffer[-1]
                    # print('took in', inBuffer[comboPos])
                    a[i + 1] = inBuffer[comboPos]
                    inBuffer[comboPos] = outBuffer[-1]
                i += 2
            elif opcode == 4:
                if instruct[-3] == '0':
                    # print(a[a[i + 1]])
                    outBuffer.append(a[a[i + 1]])
                else:
                    # print(a[i + 1])
                    outBuffer.append(a[i + 1])

                i += 2
            elif opcode == 5:
                if instruct[-3] == '0':
                    if a[a[i+1]] != 0:
                        i = a[a[i+2]] if instruct[-4] == '0' else a[i+2]
                    else:
                        i += 3
                else:
                    if a[i+1] != 0:
                        i = a[a[i+2]] if instruct[-4] == '0' else a[i+2]
                    else:
                        i += 3
            elif opcode == 6:
                if instruct[-3] == '0':
                    if a[a[i+1]] == 0:
                        i = a[a[i+2]] if instruct[-4] == '0' else a[i+2]
                    else:
                        i += 3
                else:
                    if a[i+1] == 0:
                        i = a[a[i+2]] if instruct[-4] == '0' else a[i+2]
                    else:
                        i += 3
            elif opcode == 7:
                if instruct[-3] == '0':
                    if instruct[-4] == '0':
                        if a[a[i + 1]] < a[a[i + 2]]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                    else:
                        if a[a[i + 1]] < a[i + 2]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                else:
                    if instruct[-4] == '0':
                        if a[i + 1] < a[a[i + 2]]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                    else:
                        if a[i + 1] < a[i + 2]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                i += 4
            elif opcode == 8:
                if instruct[-3] == '0':
                    if instruct[-4] == '0':
                        if a[a[i + 1]] == a[a[i + 2]]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                    else:
                        if a[a[i + 1]] == a[i + 2]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                else:
                    if instruct[-4] == '0':
                        if a[i + 1] == a[a[i + 2]]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                    else:
                        if a[i + 1] == a[i + 2]:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 1
                            else:
                                a[i+3] = 1
                        else:
                            if instruct[-5] == '0':
                                a[a[i+3]] = 0
                            else:
                                a[i+3] = 0
                i += 4

                    
            elif opcode == 99:
                break
            # print('i', i)

        comboPos += 1
    highest = max(highest, outBuffer[-1])
# print(a)
print(outBuffer)
print(highest)