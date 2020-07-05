from collections import Counter
# with open('input6_3.txt') as f:
# with open('input6_2.txt') as f:
with open('input6.txt') as f:
    given = [line.strip() for line in f]

print(given)

orbits = dict()
depths = Counter()
for i in given:
    orbitee = i[:i.index(')')]
    orbiter = i[i.index(')')+1:]
    orbits[orbiter] = orbitee
    depths[orbiter] = 0
print(orbits)
print(depths)
youPath = []
for i in orbits:
    key = i
    while key in orbits:
        if i == 'YOU':
            youPath.append(key)

        depths[i] += 1
        key = orbits[key]

sanPath = []
san = orbits['SAN']
sanPath.append(san)
while orbits[san] not in youPath:
    san = orbits[san]
    sanPath.append(san)

san = orbits[san]
sanPath.append(san)
print(depths)
print(youPath)
print(sanPath)
answer = youPath.index(sanPath[-1]) + len(sanPath) - 2
print(answer)
#part 1 answer
# print(sum(depths.values()))

#275 too low