#!/usr/local/bin/python
import sys


def extract(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print('File loaded...')

    products, users = [], []
    print('Saving products and users...')
    for l in lines:
        product, user = l.split('::')[0:2]
        print('{} / {}'.format(product, user))
        products.append(product)
        users.append(user)

    products = list(set(products))
    with open('products.dat', 'a') as products_file:
        products_file.writelines(
            ['{}\n'.format(p) for p in products]
        )

    users = list(set(users))
    with open('users.dat', 'a') as users_file:
        users_file.writelines(
            ['{}\n'.format(u)for u in users]
        )


if __name__ == "__main__":
    extract(sys.argv[1])
