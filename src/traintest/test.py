#!/usr/local/bin/python
import recsys.algorithm
import numpy as np
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
from recsys.evaluation.prediction import RMSE, MAE

# enable verbose output
recsys.algorithm.VERBOSE = True


def mass_test_and_save():

    steps = range(500, 12000501, 100000)

    for step_size in steps:
        test_and_save(step_size)

    # test_and_save('100500')


def test_and_save(step):

    mae_values, rmse_values = [], []

    # test and measure errors 5 folds
    for i in range(5):
        mae, rmse = get_mae_rmse(step)
        mae_values.append(mae)
        rmse_values.append(rmse)

    # average errors between folds
    mae_value = np.mean(mae_values)
    rmse_value = np.mean(rmse_values)

    csv_line = '{step},{mae},{rmse}\n'.format(
        step=step, mae=mae_value, rmse=rmse_value)

    with open('mae-rmse-train-test.csv', 'a') as f:
        f.write(csv_line)

    print('Wrote: {} OK'.format(csv_line))


def get_mae_rmse(step):

    data = Data()

    format = {'col': 1, 'row': 0, 'value': 2, 'ids': 'str'}

    filename = 'second_train_test.dat.{step}'.format(step=step)

    data.load(filename, sep='::', format=format)

    train, test = data.split_train_test(percent=80)

    try:

        svd = SVD('svdn_model_{step}.zip'.format(step=step))
        print('Loading model... {step}'.format(step=step))

    except:

        return

    mae_predicted, rmse_predicted = [], []
    for rating, item_id, user_id in test:
        try:

            predicted = svd.predict(item_id, user_id)

            mae_predicted.append((rating, predicted))
            rmse_predicted.append((rating, predicted))

        except:

            pass

    mae_value, rmse_value = np.nan, np.nan

    if len(mae_predicted) > 0:
        mae = MAE(mae_predicted)
        mae_value = mae.compute()

    if len(rmse_predicted) > 0:
        rmse = RMSE(rmse_predicted)
        rmse_value = rmse.compute()

    return mae_value, rmse_value


if __name__ == "__main__":
    mass_test_and_save()
