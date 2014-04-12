#!/usr/local/bin/python
import random
import numpy as np
from recsys.datamodel.data import Data
from recsys.evaluation.prediction import RMSE, MAE

# def count_reviews():
#
#     review_count = {
#         '1': 0,
#         '2': 0,
#         '3': 0,
#         '4': 0,
#         '5': 0
#     }
#
#     with open('blind.dat', 'r') as f_lines:
#         for line in f_lines:
#             values = line.split('::')
#             review_count[values[2]] += 1
#
#     return review_count

review_count = {'1': 753636,
                '2': 508291,
                '3': 845652,
                '4': 1917478,
                '5': 5864264}

# wc -l blind.dat (with .0 for float division)
total = 9889321.0

review_percentages = {'1': 0.07620705203117585,
                      '2': 0.051397967565215044,
                      '3': 0.08551163421634306,
                      '4': 0.19389379715756017,
                      '5': 0.5929895490297059}


def random_score(probDict):
    # random sample of weighted categories
    r = random.random()  # range: [0,1)
    total = 0            # range: [0,1]
    for value, prob in probDict.items():
        total += prob
        if total > r:
            return value
    raise Exception(
        'distribution not normalized: {probs}'.format(probs=probDict))


def random_test_and_save():

    data = []
    with open('blind.dat', 'r') as blind_lines:
        for line in blind_lines:
            data.append(float(line[2]))

    mae, rmse = test_random(data)

    print('"mae":"{}","rmse":"{}"'.format(mae, rmse))
    # output will be something like this
    # > "mae":"3.93757","rmse":"4.192413"


def test_random(data):

    mae_predicted, rmse_predicted = [], []
    for rating in data:
        random_predicted = float(random_score(review_percentages))
        mae_predicted.append((rating, random_predicted))
        rmse_predicted.append((rating, random_predicted))

    mae_value, rmse_value = np.nan, np.nan

    if len(mae_predicted) > 0:
        mae = MAE(mae_predicted)
        mae_value = mae.compute()

    if len(rmse_predicted) > 0:
        rmse = RMSE(rmse_predicted)
        rmse_value = rmse.compute()

    return mae_value, rmse_value


if __name__ == "__main__":
    random_test_and_save()
