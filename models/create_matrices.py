import sys


def create_matrices(key, input):
    a = []
    b = []

    matrices = {
        'a': a,
        'b': b
    }

    for line in "".join(input).split('\n'):
        values = list(map(lambda x: x.strip(), line.split(',')))
        values = list(filter(lambda x: x.isnumeric(), values))
        #yield 100, (values)
        #return
        #sys.stderr.write(str(values).encode())

        #values = list(filter(lambda x: x.isnumeric(), values))

        matrix_val = key

        #yield 100, (values)
        if len(values) != 3:
            break

        row, column, value = list(map(lambda x: int(x), values))

        matrix = matrices[matrix_val]
        if len(matrix) > row:
            matrix[row] += [value]
        else:
            matrix.append([value])

    return matrices
