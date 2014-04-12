from __future__ import print_function
import sys
import random


def save_lines(lines, filename):

    with open(filename, 'a') as f:

        f.writelines(
            ['{}\n'.format(l) for l in lines]
        )

        print('File written: {}'.format(filename))


def slice(filename):

    with open(filename) as f:
        lines = f.read().splitlines()

    print('File loaded...')

    steps = range(500, len(lines), 100000)

    for step_size in steps:
        sample = random.sample(lines, step_size)
        save_lines(sample, '{}.{}'.format(filename, step_size))


if __name__ == "__main__":
    slice(sys.argv[1])
