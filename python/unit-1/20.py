A = []
B = []
C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

print("Enter elements of Matrix A:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"A[{i}][{j}] = ")))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"B[{i}][{j}] = ")))
    B.append(row)

# Matrix multiplication
for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

print("Result of Matrix Multiplication:")
for i in range(3):
    for j in range(3):
        print(C[i][j], end=" ")
    print()
