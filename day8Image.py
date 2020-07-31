import re
file = open("input8.txt", 'r')
a = file.read()
# a = "123456789012"
# a = "0222112222120000"
width = 25
# width = 2
height = 6
# height = 2
layers = [a[i*width*height:(i+1)*(width*height)] for i in range(len(a)//(width*height))]
# layers = []
# for i in range(len(a) //(width*height)):
#     layers.append(a[i*width*height: (i+1)*width*height])
print(layers)
# for i in range(len(layers)):
#     # print(re.findall('[0-2]'*width, layers[i]))
#     layers[i] = re.findall('[0-2]'*width, layers[i])
# print(layers)
# for i in layers:
depth= 0
pos = 0
answer = ""
while pos < width * height:
    while layers[depth][pos] == "2":
        depth += 1
        # if depth >= len(layers):

    answer += layers[depth][pos]
    pos+=1
    depth = 0
picture = re.findall('[0-2]'*width, answer)
print(picture)
for i in picture:
    i = i.replace("1", "#")
    i = i.replace("0", " ")
    print("".join(i))
    
#part 1
# fewest = min(layers, key=lambda x: x.count("0"))
# index = layers.index(fewest)
# print(fewest)
# print(index)
# oneCount = layers[index].count("1")
# twoCount = layers[index].count("2")
# print(oneCount, "*", twoCount, oneCount * twoCount)

# for i in layers:
#     i =[[i[j:j+width] for j in range(0, width*height + 1, width)]]
# print(layers)