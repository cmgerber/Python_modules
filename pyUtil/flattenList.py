import itertools


def flatten(in_list):
    return list(itertools.chain(*in_list))
