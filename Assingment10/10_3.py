import numpy as np

def generate_magic_square_odd(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n*n + 1):
        magic_square[i, j] = num
        i -= 1
        j += 1
        if num % n == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j == n:
            j = 0
    return magic_square

def generate_magic_square_doubly_even(n):
    magic_square = np.arange(1, n*n + 1).reshape(n, n)
    indices = np.array([[i, j] for i in range(n) for j in range(n)
                        if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3)])
    for i, j in indices:
        magic_square[i, j] = n*n + 1 - magic_square[i, j]
    return magic_square

def generate_magic_square_singly_even(n):
    half_n = n // 2
    sub_square_size = half_n * half_n
    sub_magic = generate_magic_square_odd(half_n)

    magic_square = np.zeros((n, n), dtype=int)

    # Quadrants: A, B, C, D
    A = sub_magic
    B = sub_magic + 2 * sub_square_size
    C = sub_magic + 3 * sub_square_size
    D = sub_magic + sub_square_size

    magic_square[:half_n, :half_n] = A
    magic_square[:half_n, half_n:] = B
    magic_square[half_n:, :half_n] = C
    magic_square[half_n:, half_n:] = D

    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(n):
            if (j < k or j >= n - k) or (j == k and i == k):
                if j < half_n:
                    magic_square[i, j], magic_square[i + half_n, j] = \
                        magic_square[i + half_n, j], magic_square[i, j]
    return magic_square

# Generate and print magic squares for N=4 to 8
for n in [4, 5, 6, 7, 8]:
    if n % 2 == 1:
        square = generate_magic_square_odd(n)
    elif n % 4 == 0:
        square = generate_magic_square_doubly_even(n)
    else:
        square = generate_magic_square_singly_even(n)
    print(f"Magic Square (N={n}):\n{square}\n")
