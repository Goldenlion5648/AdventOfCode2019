from math import *
RAW = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''

conversions = dict()
given = RAW.split('\n')
print(given)
for i in given:
    print(i)
    result = (i[i.index('=>')+2:].strip()).split(' ')
    result[0] = int(result[0])
    value = (i[:i.index('=>')].strip().split(', '))
    # value = tuple(map(tuple, value))
    for j in range(len(value)):
        i = value[j]
        i = tuple(i.split(' '))
        # print("i", i)
        value[j] = i
    # value = tuple(value)

    print("result", result)
    conversions[tuple(result)] = value
print(conversions)

required = []
required += conversions[(1, 'FUEL')]
print(required)
# for i in range(len(required)):
pos = 0
amountsNeeded = dict()
while pos < len(required):
    keyToSearchFor = required[pos][1]
    print('keyToSearchFor', keyToSearchFor)
    for key in conversions:
        if key[1] == keyToSearchFor:
            # print('conversionKey', conversions[key])
            repeatTimes = ceil(int(required[pos][0])/key[0])
            print("repeatTimes", repeatTimes)
            for x in range(repeatTimes):
                [required.append(k) for k in conversions[key]]
            required.pop(0)
            break
    shouldKeepSearching = False
    for i in required:
        if i[1] != 'ORE':
            shouldKeepSearching = True
            break
    if shouldKeepSearching == False:
        break

    print(required)

# while "ORE" not in required[0]:
#     for key in conversions
#     required.append()
print(required)
required = [(int(i[0]), i[1]) for i in required]
print(required)
print(sum([i[0] for i in required]))
# with open('input14.txt') as f:
#     given = [line.strip() for line in f]
# print(given) 