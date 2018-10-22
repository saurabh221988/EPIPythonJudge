from epi_judge_python.test_framework import generic_test


def reverse_bits(x):
    # TODO - you fill in here.
    bitstring = '{0:b}'.format(x)
    bitstring = '0' * (64 - len(bitstring)) + bitstring
    rev = bitstring[::-1]
    num = int(rev, 2)
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
