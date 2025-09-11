def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix dimensions do not match for multiplication")

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Input matrices
rows_A = int(input("Enter rows for Matrix A: "))
cols_A = int(input("Enter cols for Matrix A: "))
print("Enter Matrix A row by row:")
A = [list(map(int, input().split())) for _ in range(rows_A)]

rows_B = int(input("Enter rows for Matrix B: "))
cols_B = int(input("Enter cols for Matrix B: "))
print("Enter Matrix B row by row:")
B = [list(map(int, input().split())) for _ in range(rows_B)]

try:
    product = multiply_matrices(A, B)
    print("Result of Matrix Multiplication:")
    for row in product:
        print(row)
except ValueError as e:
    print(e)
