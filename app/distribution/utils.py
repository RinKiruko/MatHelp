def normalize(z, seq):
    return (z - min(seq)) / (max(seq) - min(seq))


def get_criterion(category_metrics):
    return 6 * category_metrics['count'] + category_metrics['weight'] + category_metrics['proportion']
