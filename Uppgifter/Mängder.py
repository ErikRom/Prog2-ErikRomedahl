a = set()

b = set()

a.add("Banan")
a.add("Päron")
a.add("Äpple")

b.add("Kiwi")
b.add("Ananas")
b.add("Päron")

c = set()

c = c.union(a, b)

print(c)