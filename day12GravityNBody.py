a = '''<x=0, y=6, z=1>
<x=4, y=4, z=19>
<x=-11, y=1, z=8>
<x=2, y=19, z=15>'''
positions = a.split('\n')
# print(positions)

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
c = []
for i in range(0, len(b), 3):
    c.append(b[i:i+3].copy())

print(c)
velocities =[[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
print(velocities)
potential = 0
kinetic = 0
for t in range(1000):
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
    # print(c)
for i in range(len(c)):
    potential += sum(list(map(abs, c[i]))) * sum(list(map(abs, velocities[i])))

# print(potential)
# print(kinetic)
print(potential )
