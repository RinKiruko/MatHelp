import pickle

from django.views.generic import View

from openpyxl import load_workbook


class Distribute(View):
    def get(self, request, *args, **kwargs):
        # %%



        wb = load_workbook(filename="./datasets/test.xlsx")
        ws = wb['Data']

        payments = {row[0].value: row[1].value for row in ws.rows if row[0].value is not None}
        budget = 407500
        wb.close()

        normalize = lambda z, seq: (z - min(seq)) / (max(seq) - min(seq))

        get_criterion = lambda category_metrics: category_metrics['count'] * 6 + category_metrics['weight'] + \
                                                 category_metrics['proportion']

        # %%

        import math

        avg_proportion = {}
        for category in weights:
            sum_ = sum([math.pow(payment[4] / payment[5], 2) for payment in dataset if payment[0] == category])
            len_ = len([payment for payment in dataset if payment[0] == category])
            avg_proportion[category] = math.sqrt(sum_ / len_) if len_ > 0 else 0

        rel_counts = {
            category: count / sum(payments.values())
            for category, count in payments.items()
        }
        rel_weights = {
            category: weights[category] / sum([value for key, value in weights.items() if key in payments])
            for category in payments
        }
        test_metrics = {
            category: {
                'count': normalize(rel_counts[category], rel_counts.values()),
                'proportion': normalize(avg_proportion[category], avg_proportion.values()),
                'weight': normalize(rel_weights[category], rel_weights.values())
            } for category, count in payments.items() if count
        }

        estimated = {
            category: get_criterion(test_metrics[category])
            for category in payments
        }

        # %%
        distributions = {
            category: {
                'received': budget * (estimated[category] / sum(estimated.values())),
            } for category, count in payments.items()
        }

        print()
