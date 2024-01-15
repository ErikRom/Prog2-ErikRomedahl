def add(a, b, c):
    sum = a + b
    if sum == c:
        return "correct!"
    else:
        return "wrong!"

n = input()
a, b, c = n.split()

a = int(a)
b = int(b)
c = int(c)

print(add(a, b, c))