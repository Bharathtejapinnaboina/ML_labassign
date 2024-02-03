def matrix_power(A, power):
    order = len(A)
    identity_matrix = [[1 if i == j else 0 for j in range (order)] for i in range(order)]

    for _ in range(power):
        identity_matrix = matrix_multiply(identity_matrix, A)

    return identity_matrix 

def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Matrices cannot be multiplied.")
        return None
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range (cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

matrix_A = [[1, 2, 3], [5, 6, 7], [1, 2, 4]]
power_value = 4

result_matrix = matrix_power(matrix_A, power_value)
print(result_matrix)

