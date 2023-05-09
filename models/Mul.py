from mrjob.job import MRJob
from create_matrices import create_matrices


# noinspection PyRedundantParentheses
class Mul(MRJob):

    def mapper(self, _, line):
        values = line.split(',')
        key = values.pop(0)

        yield (f"d", (f"{key},{','.join(values)}\n"))

    def reducer(self, key, values):
        transformed_values = ','.join(values).split('\n')

        a_values = list(map(lambda x: x.replace('a,', ''), filter(lambda x: "a" in x, transformed_values)))
        a_values = ','.join(a_values).replace(',,', '\n')

        a = create_matrices('a', a_values)['a']

        b_values = list(map(lambda x: x.replace('b,', ''), filter(lambda x: "b" in x, transformed_values)))
        b_values = ','.join(b_values).replace(',,', '\n')
        b = create_matrices('b', b_values)['b']

        c = []
        columns = list(zip(*b))

        for row in range(len(a)):
            values = []
            for col in range(len(a[row])):
                row_v = a[row]
                col_v = columns[col]

                prod = [row_v[x] * col_v[x] for x in range(len(row_v))]

                values += [sum(prod)]

            c += [values]

        yield ("c", (f"{c}"))


if __name__ == '__main__':
    Mul().run()
