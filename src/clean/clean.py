#!/usr/local/bin/python
import sys

# original data is like this
# ===============================================
# product/productId: B000068VBQ
# product/title: Fisher-Price Rescue Heroes: Lava Landslide
# product/price: 8.88
# review/userId: A10P44U29RNOT6
# review/profileName: D. Jones
# review/helpfulness: 6/6
# review/score: 1.0
# review/time: 1126742400
# review/summary: Doesn't work on a Mac
# review/text: blah blah blah
# ===============================================


def clean(filename):
    with open(filename) as f:
        review = {}
        for line in f:
            line = line.strip()
            # empty lines mean separation between reviews
            if len(line) <= 1:
                # do not save reviews with unknown user ids
                if 'unknown' not in review['user_id']:
                    print('{}::{}::{}::{}::{}::{}'.format(
                        review['product_id'],
                        review['user_id'],
                        int(review['score'][0]),
                        review['price'],
                        review['helpfulness'],
                        review['time']
                    ))
                # reset review for the next iteration
                review = {}
                continue
            category, value = line.split(':', 1)
            value = value.strip()
            if 'product/productId' in category:
                review['product_id'] = value
            if 'review/userId' in category:
                review['user_id'] = value
            if 'product/price' in category:
                review['price'] = value
            if 'review/helpfulness' in category:
                review['helpfulness'] = value
            if 'review/time' in category:
                review['time'] = value
            if 'review/score' in category:
                review['score'] = value

# processed data looks like this
# ===============================================
# review/userId::product/productId::review/score
# A2NYK9KWFMJV4Y::B000063W5A::5.0
# ===============================================

if __name__ == "__main__":
    clean(sys.argv[1])
