from collections import deque
from collections import Counter
import math
import copy
from tqdm import *
#780827090544 is too low

def lcm(x, y):
    return x * y // math.gcd(x, y)

a = '''<x=0, y=6, z=1>
<x=4, y=4, z=19>
<x=-11, y=1, z=8>
<x=2, y=19, z=15>'''

# a='''<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>'''

#example 1
# a = '''<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>'''
positions = a.split('\n')
# print(positions)
seen = deque()
# positions = list(map(split(','), positions)
for i in range(len(positions)):
    positions[i] = positions[i].replace('<','')
    positions[i] = positions[i].replace('>','')
    positions[i] = positions[i].split(',')
# positions = [i[i.index('='):] for i in positions]
# print(positions)
b = []
for i in positions:
    b += i
# positions = "".join(positions)

# print(b)
b = [i[i.index('=')+1:] for i in b]
# print(b)
b=  list(map(int, b))
c = deque()
for i in range(0, len(b), 3):
    c.append(b[i:i+3].copy())

print(c)
velocities =deque([[0,0,0], [0,0,0], [0,0,0], [0,0,0]])
print(velocities)
potential = 0
kinetic = 0
posesSeen = [deque() for i in range(4)]
velocitiesSeen = [deque() for i in range(4)]
z = (copy.deepcopy(c), copy.deepcopy(velocities))
seen.append(z)
posRepeatTimes = [Counter() for i in range(4)]
velocityRepeatTimes= [Counter() for i in range(4)]
foundXYZ = []
for t in trange(500000):
    for j in range(len(c)):
        for i in range(len(c)):
            if j == i:
                continue
            # if c[j] < c[i]:
            for n in range(3):
                # print('ran')
                # print('before',velocities[j][n], c[j][n], c[i][n])
                if c[j][n] - c[i][n] < 0:
                    velocities[j][n] += 1
                elif c[j][n] - c[i][n] > 0:
                    velocities[j][n] -= 1
                # print('after',velocities[j][n], c[j][n], c[i][n])
            # print(velocities)
    for i in range(len(velocities)):
        for n in range(3):
            c[i][n] += velocities[i][n]
    # if t % 5000 == 0:
    #     print(t)
    # if t > 2750:
    #     print(t)
    #     print('positions', c)
    #     print('vel',velocities)
    for k in range(3):
        if k in foundXYZ:
            continue
        p1 = []
        v1 = []
        for q in range(4):
            p1.append(c[q][k])
            v1.append(velocities[q][k])
        both = (tuple(p1), tuple(v1))
        if posRepeatTimes[k][both] == 1 or posRepeatTimes[k][both] == 0:
            posRepeatTimes[k][both] += 1
            posesSeen[k].append(both)
        else:
            foundXYZ.append(k)
        # v1 = copy.deepcopy(velocities[k])

        # velocityRepeatTimes[k][tuple(v1)] += 1
        # velocitiesSeen[k].append(tuple(v1))
        # if p1 not in posesSeen[k]:
        #     posesSeen[k].append(p1)
        # else:
        #     # print(posesSeen[-1])
        #     posesSeen[k].append(p1)
            # print(p1)

    # for k in range(4):

        # if v1 not in velocitiesSeen[k]:
        #     velocitiesSeen[k].append(v1)
        # else:
        #     # print(posesSeen[-1])
        #     velocitiesSeen[k].append(v1)
            # print(p1)
        # pass
    # if(t % 1000 == 0):
    #     print(t)
    # if t == 12000:
    #     total = 1
    #     for k in range(4):
    #         commonVel =velocityRepeatTimes[k].most_common(3) 
    #         commonPos = posRepeatTimes[k].most_common(3)
    #         print(commonVel)
    #         print(commonPos)
    #         # if total == 1:
    #         #     total = lcm(commonVel[0][0], commonPos[0][0])
    #         #     print(total)
    #         total = lcm(total, commonVel[0][0])
    #         total = lcm(total, commonPos[0][0])
    #     print(total)
    #     break
total = 1
for k in range(3):
    # commonVel =velocityRepeatTimes[k].most_common(3) 
    commonPos = posRepeatTimes[k].most_common(3)
    # print(commonVel)
    print(commonPos)
    print(commonPos[0][0])
    # first = velocitiesSeen[k].index(commonVel[0][0])
    # second = velocitiesSeen[k].index(commonVel[0][0], first + 1)
    # print(second - first)
    firstPos = posesSeen[k].index(commonPos[0][0])
    secondPos = posesSeen[k].index(commonPos[0][0], firstPos + 1)
    print(firstPos)
    print(secondPos)
    print(secondPos - firstPos)
    total = lcm(total, secondPos - firstPos)
print(total)
    # print(secondPos - firstPos)
    # if total == 1:
    #     total = lcm(commonVel[0][0], commonPos[0][0])
    #     print(total)
    # total = lcm(total, commonVel[0][0])
    # total = lcm(total, commonPos[0][0])
# print(total)
    #     # print(velocitiesSeen)
    #     print(posesSeen)
    #     break
        # print('saw same velocity')
        # print(t)
    #     # break
    # z = (copy.deepcopy(c), copy.deepcopy(velocities))
    # if z not in seen:
    #     seen.append(z)
    #     # print(seen)
    # else:
    #     # pass
    #     print(t)
    #     print(z)
    #     print(seen[-1])
    #     # print(seen[0])
    #     break
    # print(c)
# for i in range(len(c)):
#     potential += sum(list(map(abs, c[i]))) * sum(list(map(abs, velocities[i])))
# print(seen)
# print(potential)
# print(kinetic)
# print(potential )
