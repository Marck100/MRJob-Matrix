from mrjob.job import MRJob
from create_matrices import create_matrices


# noinspection PyRedundantParentheses
class Add(MRJob):

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

        for row in range(len(a)):
            values = []
            for col in range(len(a[row])):
                values += [a[row][col] + b[row][col]]

            c += [values]

        yield ("c", (f"{c}"))


if __name__ == '__main__':
    Add().run()
