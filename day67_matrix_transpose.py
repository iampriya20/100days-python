matrix = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

print("Original Matrix:")
for r in matrix:
    print(r)

print("Transposed Matrix:")
for r in transpose:
    print(r)
