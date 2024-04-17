import csv

with open('teams.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    points = [0]
    teams = [0]
    allTeams5on4  = {}


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
            allTeams5on4.append({
                "team": row[3],
                "points": float(row[7])
            })
        sortedTeams = sorted(allTeams5on4.items(), key=lambda x:x[1], reverse=True)

        for key, value in sortedTeams[:10]:
            print(key)

print(f"Best team: {teams[0]}")
