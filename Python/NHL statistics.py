import csv
lag = []


with open('teams.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    points = [0]
    teams = [0]
    points2 = []
    teams2 = []
    for row in csv_reader:
        if row[5] == 'all':
            points.append(row[12])
            teams.append(row[3])
            if float(points[0]) < float(points[1]):
                points.pop(0)
                teams.pop(0)
            else:
                points.pop(1)
                teams.pop(1)
        if row[5] == '5on4':
            if len(points2) < 10:
                points2.append(row[12])
                teams2.append(row[3])
            else:
                for i in points2:
                    print(points2)
                    i = float(points[i])
                    if float(row[12]) > float(points2[i]):
                        points2.pop(i)
                        points2.append(i)
                        teams2.pop(i)
                        teams2.pop(i)
print(f"Best team: {teams[0]}")
print(teams2)