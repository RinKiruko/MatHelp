import typing


def normalize(z, seq: typing.Iterable):
    return (z - min(seq)) / (max(seq) - min(seq))


def get_criterion(category_metrics):
    return 6 * category_metrics['count'] + category_metrics['weight']
