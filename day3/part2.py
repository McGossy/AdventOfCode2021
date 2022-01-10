data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append(line[:-1])

def life_support_generator(oxy_bits, co2_bits, n):
    collected_oxy_bits = []
    collected_co2_bits = []

    for i in range(len(oxy_bits)):
        collected_oxy_bits.append(oxy_bits[i][n])
    for i in range(len(co2_bits)):
        collected_co2_bits.append(co2_bits[i][n])

    oxy_bits_charge = '1' if collected_oxy_bits.count('1') >= collected_oxy_bits.count('0') else '0'
    co2_bits_charge = '0' if collected_co2_bits.count('1') >= collected_co2_bits.count('0') else '1'

    oxy_gen = []
    co2_gen = []
    for i in range(len(oxy_bits)):
        if oxy_bits[i][n] == oxy_bits_charge:
            oxy_gen.append(oxy_bits[i])
    for i in range(len(co2_bits)):
        if co2_bits[i][n] == co2_bits_charge:
            co2_gen.append(co2_bits[i])
    return oxy_gen, co2_gen


oxy_gen = data
co2_gen = data
final_oxy = 0
final_co2 = 0
for i in range(len(data[0])):
    oxy_gen, co2_gen = life_support_generator(oxy_gen, co2_gen, i)
    print("\noxy_gen:", oxy_gen)
    print("co2_gen:", co2_gen)
    if len(oxy_gen) == 1:
        final_oxy = int(oxy_gen[0], 2)
    if len(co2_gen) == 1:
        final_co2 = int(co2_gen[0], 2)

print(final_oxy)
print(final_co2)

final_life_rating = final_oxy * final_co2
print(final_life_rating)



