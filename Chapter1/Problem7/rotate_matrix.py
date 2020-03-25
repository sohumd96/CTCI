def rotate_matrix(matrix):

    for i in range(0, len(matrix)//2):
        for j in range(i, len(matrix) - 1 - i):
            end = len(matrix)-1 - j
            temp = matrix[i][j]
            matrix[i][j] = matrix[end][i]
            matrix[end][i] = matrix[len(matrix)-1-i][end]
            matrix[len(matrix)-1-i][end] = matrix[j][len(matrix)-1-i]
            matrix[j][len(matrix)-1-i] = temp

    return matrix