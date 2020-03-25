def zero_matrix(matrix):
    def zero_col(matrix, col):
        for i in range(0, len(matrix)):
            matrix[i][col] = 0
    def zero_row(matrix, row):
        for i in range(0, len(matrix[0])):
            matrix[row][i] = 0

    bool_row = False
    bool_col = False

    for i in range(0, len(matrix[0])):
        if matrix[0][i] == 0 :
            bool_row = True
            break
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0 :
            bool_col = True
            break

    for i in range(1, len(matrix)):
        for j in range (1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix[0])):
        if matrix[0][i] == 0:
            zero_col(matrix,i)
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0 :
            zero_row(matrix,i)

    if bool_row:
        zero_row(matrix, 0)
    if bool_col:
        zero_col(matrix, 0)

    return matrix