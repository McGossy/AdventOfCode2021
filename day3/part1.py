data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append(line[:-1])

print(data)
rows = [[] for i in range(len(data[0]))]
print(rows)


for i in range(len(data)):
    for j in range(len(data[i])):
        rows[j].append(data[i][j])

print(rows)
gamma_rate = ""
epsilon_rate = ""
print("proper output:")
for row in rows:
    if row.count('1') > row.count('0'):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate)
print(epsilon_rate)

power_consumption = gamma_rate * epsilon_rate
print("power consumption: ", power_consumption)

