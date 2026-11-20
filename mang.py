file = open("visits.csv", "r", encoding='utf-8')

for row in file:
    print(row)

    file.close()