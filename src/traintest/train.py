#!/usr/local/bin/python
import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data

# enable verbose output
recsys.algorithm.VERBOSE = True


def mass_train_and_save():

    steps = range(500, 12000501, 100000)

    for step_size in steps:
        filename = 'second_train_test.dat.{}'.format(step_size)
        train_and_save(filename)


def train_and_save(filename):

    step = filename.split('.')[-1]

    data = Data()

    format = {'col': 1, 'row': 0, 'value': 2, 'ids': 'str'}
    data.load(filename, sep='::', format=format)

    train, test = data.split_train_test(percent=80)

    try:

        svd = SVD('svdn_model_{step}.zip'.format(step=step))
        print('Already exists: svdn_model_{step}.zip'.format(step=step))

    except:

        svd = SVD()
        svd.set_data(train)

        svd.compute(
            k=100,
            min_values=2,
            pre_normalize=False,
            mean_center=True,
            post_normalize=True,
            savefile='svdn_model_{step}'.format(step=step)
        )

        print('Saved svdn_model_{step}.zip'.format(step=step))


if __name__ == "__main__":
    mass_train_and_save()
