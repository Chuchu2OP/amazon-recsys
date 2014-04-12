#!/usr/local/bin/python
import sys

# original data is like this
# ===============================================
# review/userId::product/productId::review/score
# A2NYK9KWFMJV4Y::B000063W5A::5.0
# ===============================================
#
# map-reduce job counted user reviews like this
# "AXJTNYD3UK1BP"   13


def filter(users_file, rows_file):
    users = []
    with open(users_file) as f:
        for line in f:
            line = line.strip()
            user_id, num_reviews = line.split()
            # keep the user id, but clean
            users.append(user_id[1:-1])

    with open(rows_file) as f:
        for line in f:
            line = line.strip()
            user_id, product_id, score = line.split('::')
            if user_id in users:
                # we keep the line if it's a "valid" user
                print(
                    '{}::{}::{}'.format(user_id, product_id, score)
                )

if __name__ == "__main__":
    filter(sys.argv[1], sys.argv[2])
