matrix = []
for line in open("input.txt"):
    row = line.split()
    for i,val in enumerate(row):
        row[i] = float(val)
    matrix.append(row)

for line in open("input.txt"):
    matrix.append(list(map(float,line.split())))

print(matrix)