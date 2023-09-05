def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    row, col = 0, n // 2

    for num in range(1, n**2 + 1):
        magic_square[row][col] = num
        row -= 1
        col += 1

        if num % n == 0:
            row += 2
            col -= 1
        elif row < 0:
            row = n - 1
        elif col == n:
            col = 0

    return magic_square

def print_magic_square(square):
    n = len(square)
    for i in range(n):
        row_str = ' '.join(map(lambda x: str(x).rjust(3), square[i]))
        print(row_str)
        
if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the magic square (odd): "))
        if n < 1 or n % 2 == 0:
            print("Please enter a positive odd integer.")
        else:
            magic_square = generate_magic_square(n)
            print("Magic Square of size", n)
            print_magic_square(magic_square)

    except ValueError:
        print("Invalid input. Please enter a positive odd integer for the size.")





