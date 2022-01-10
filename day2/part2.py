data = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        line[1] = int(line[1])
        data.append(line)

h_pos = 0
d_pos = 0
aim = 0

for i in range(len(data)):
    direction = data[i][0]
    movement = data[i][1]

    if direction == 'forward':
        h_pos += movement
        d_pos += aim * movement
    if direction == 'up':
        aim -= movement
    if direction == 'down':
        aim += movement
    print(h_pos, d_pos, aim)

print(h_pos * d_pos)
