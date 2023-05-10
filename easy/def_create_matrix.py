def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = i + 1
            elif i < j:
                matrix[i][j] = up_fill
            else:
                matrix[i][j] = down_fill
    return matrix

# The create_matrix function returns a size x size square matrix with numbers from 1
# to size on the diagonal. All other elements are filled according
# to the up_fill and down_fill parameters