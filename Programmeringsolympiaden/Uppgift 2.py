def triplet(N):
    list = []
    for number in range(1,N):
        treigt_tal = (number)*(number+1)*(number+2)
        if treigt_tal <= N:
            list.append(treigt_tal)
    print(f"Svar: {len(list)}")

N = input("N: ")
N = int(N)

triplet(N)