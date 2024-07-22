import math
import collections

ENTROPY_THRESHOLD = 5.1


def calculate_entropy(data):
    # frequency of each character in the data
    char_counts = collections.Counter(data)
    total_chars = len(data)

    # calculate probability of appearance for each character
    probabilities = list()
    for count in char_counts.values():
        probabilities.append(count / total_chars)

    # compute entropy
    entropy = 0
    for p in probabilities:
        entropy = entropy - (p * math.log2(p))

    return entropy
