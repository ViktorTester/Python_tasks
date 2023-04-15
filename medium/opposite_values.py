n, m = map(int, input().split())
matrix1, matrix2 = [], []
counter = 0

for _ in range(n):
    row = list(input())
    matrix1.append(row)

k = input()

for _ in range(n):
    row = list(input())
    matrix2.append(row)

for i in range(n):
    for j in range(m):
        if matrix1[i][j] == matrix2[i][j]:
            counter += 1

print(counter)

# The program compares two images consisting of black and white pixels.
# The pixels in the second image must be the opposite color of the
# pixels in the first image. The program counts the number of pixels in
# the second image that are not opposite in color.

# The program first reads the numbers n and m - the height and width of the original
# image. The next n lines contain a description of the original image. Each line
# consists of m characters "B" and "W". The symbol "B" corresponds to black,
# and the symbol "W" corresponds to white. This is followed by a blank line followed
# by a description of the image in the same format as the original image.