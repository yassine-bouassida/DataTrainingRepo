#https://www.codewars.com/kata/5919f3bf6589022915000023

def rotate_matrix(matrix, times_to_turn):
    n = times_to_turn % 4  # avoid unnecessary rotations

    for _ in range(n):
        matrix = [list(row) for row in zip(*matrix)][::-1]

    return matrix
