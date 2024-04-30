def is_perfect_square(n):
    sqrt_n = int(n**0.5)
    return n == sqrt_n * sqrt_n

def is_fibonacci_number(number):
    if number < 0:
        return False
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

def find_fibonacci_index(number):
    if number < 0:
        return None
    a, b = 0, 1
    index = 0
    while a < number:
        a, b = b, a + b
        index += 1
    return index if a == number else None

with open('input.txt', 'r') as file:
    given_number = int(file.readline().strip())

with open('output.txt', 'w') as file:
    if is_fibonacci_number(given_number):
        file.write(f"{given_number} Фибоначчийн тоо юм.\n")
        index = find_fibonacci_index(given_number)
        file.write(f"Энэ бол Фибоначчийн{index}-р дарааллын дугаар.\n")
    else:
        file.write(f"{given_number} Фибоначчийн тоо биш.\n")
