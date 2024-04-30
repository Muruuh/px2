from math import gcd

def subtract_fractions(a, b, c, d):
    common_denominator = b * d
    numerator1 = a * (common_denominator // b)
    numerator2 = c * (common_denominator // d)

    result_numerator = numerator1 - numerator2

    common_divisor = gcd(result_numerator, common_denominator)
    result_numerator //= common_divisor
    common_denominator //= common_divisor

    return result_numerator, common_denominator

def read_fractions(file_path):
    with open(file_path, 'r') as file:
        fractions = file.readline().split()
        return int(fractions[0]), int(fractions[1]), int(fractions[2]), int(fractions[3])

def write_result(file_path, result):
    with open(file_path, 'w') as file:
        file.write(f"{result[0]}/{result[1]}\n")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    a, b, c, d = read_fractions(input_file)

    result = subtract_fractions(a, b, c, d)

    write_result(output_file, result)
