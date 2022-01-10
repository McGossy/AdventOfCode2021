data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append(int(line))


larger_than = 0
for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        larger_than += 1

print(larger_than)


