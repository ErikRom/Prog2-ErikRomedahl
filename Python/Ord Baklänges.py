ord = list(input("Skriv ditt or här: "))

nytt_ord = ""

for _ in range(len(ord)):
    nytt_ord += ord[-1]
    ord.pop(-1)

print(nytt_ord)