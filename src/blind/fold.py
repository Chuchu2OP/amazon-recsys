from __future__ import print_function
# import numpy
# import pandas
# import pylab
import sys
from random import shuffle
# from sklearn.cross_validation import KFold


def kfold(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print('File loaded...')

    x = range(len(lines))
    print('Range ready...')

    shuffle(x)
    print('Range shuffled...')

    blind_indexes = x[:int(len(lines)/3)-1]
    print('Blind indexes set...')

    blinds = [lines[x[i]] for i in blind_indexes]
    print('Blind points found...')

    with open('blind.dat', 'a') as blind_file:
        blind_file.writelines(
            [l + '\n' for l in blinds]
        )
    print('File: blind.dat Ready')

    test_train_indexes = x[int(len(lines)/3):]
    print('Test/Train indexes set')

    test_train = [lines[x[i]] for i in test_train_indexes]
    print('Test/Train points found...')

    with open('train_test.dat', 'a') as train_test_file:
        train_test_file.writelines(
            [l + '\n' for l in test_train]
        )
    print('File: train_test.dat Ready')


if __name__ == "__main__":
    kfold(sys.argv[1])
