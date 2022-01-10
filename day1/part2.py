data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append(int(line))


larger_than = 0
for i in range(len(data) - 3):
    window = data[i] + data[i+1] + data[i+2]
    window2 = data[i + 1] + data[i+2] + data[i+3]
    if window < window2:
        larger_than += 1
print(larger_than)


