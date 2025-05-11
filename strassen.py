def multiply(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
    
    n = len(A) // 2
    A11, A12, A21, A22 = [row[:n] for row in A[:n]], [row[n:] for row in A[:n]], [row[:n] for row in A[n:]], [row[n:] for row in A[n:]]
    B11, B12, B21, B22 = [row[:n] for row in B[:n]], [row[n:] for row in B[:n]], [row[:n] for row in B[n:]], [row[n:] for row in B[n:]]
    
    def add(X, Y):
        return[ [X[i][j] + Y[i][j] for j in range(len(X))] for i in range(len(X)) ]
    
    def subtract(X, Y):
        return[ [X[i][j] - Y[i][j] for j in range(len(X))] for i in range(len(X)) ]
    
    M1 = multiply(add(A11, A22), add(B11, B22))
    M2 = multiply(add(A21, A22), B11)
    M3 = multiply(A11, subtract(B12, B22))
    M4 = multiply(A22, subtract(B21, B11))
    M5 = multiply(add(A11, A12), B22)
    M6 = multiply(subtract(A21, A11), add(B11, B12))
    M7 = multiply(subtract(A12, A22), add(B21, B22))
    
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)
    
    C = [C11[i] + C12[i] for i in range(n)] + [C21[i] + C22[i] for i in range(n)]
    return C


n = int(input("Enter size of matrix: "))
print("Enter matrix 1: ")
A = [list(map(int, input().split())) for _ in range(n)]
print("Enter matrix 2: ")
B = [list(map(int, input().split())) for _ in range(n)]

result = multiply(A, B)


print("Resulting matrix: ")
for row in result:
    print(" ".join(map(str, row)))