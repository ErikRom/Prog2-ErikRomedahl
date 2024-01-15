def twentyfortyeight():
    a


line = input()
line1 = input()
line2 = input()
line3 = input()
direction = input()

a, b, c, d = line.split()
a1, b1, c1, d1 = line1.split()
a2, b2, c2, d2 = line2.split()
a3, b3, c3, d3 = line3.split()

if direction == 0:
    if line[0] == line[1]:
        line[0] = line[0] + line[1]
        line[1] = line[2]
        line[2] = line[3]
        line[3] = 0
    if line[1] == line[2]:
        line[1] = line[1] + line[2]
        line[2] = line[3]
        line[3] = 0
    if line[2] == line[3]
        line[2] = line[2] + line[3]
        line[3] = 0



elif direction == 1:


elif direction == 2:


elif direction == 3:



print(line)
print(line1)
print(line2)
print(line3)