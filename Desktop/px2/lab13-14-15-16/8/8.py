class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

def read_complex_number(file):
    real, imag = map(float, file.readline().split())
    return ComplexNumber(real, imag)

def write_result(file, result):
    file.write(result + '\n')

with open('input.txt', 'r') as input_file:
    complex1 = read_complex_number(input_file)
    complex2 = read_complex_number(input_file)

result = "Тэнцүү" if complex1 == complex2 else "Тэнцүү биш"

with open('output.txt', 'w') as output_file:
    write_result(output_file, result)
