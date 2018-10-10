from epi_judge_python.test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


def parity_brute(x):
    # TODO - you fill in here.
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count % 2


def parity_brute2(x):
    # TODO - you fill in here.
    count = 0
    while x:
        count ^= x & 1
        x >>= 1
    return count


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
