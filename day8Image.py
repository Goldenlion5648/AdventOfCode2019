file = open("input8.txt", 'r')
a = file.read()
# a = "123456789012"
a = "0222112222120000"
width = 25
height = 6
# layers = [a[i*width:i+width] for i in range(height)]
layers = []
for i in range(len(a) //(width*height)):
    layers.append(a[i*width*height: (i+1)*width*height])
print(layers)
fewest = min(layers, key=lambda x: x.count("0"))
index = layers.index(fewest)
print(fewest)
print(index)
oneCount = layers[index].count("1")
twoCount = layers[index].count("2")
print(oneCount, "*", twoCount, oneCount * twoCount)

# for i in layers:
#     i =[[i[j:j+width] for j in range(0, width*height + 1, width)]]
# print(layers)