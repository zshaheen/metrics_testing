import cdp_metric

class Add(cdp_metric.CDPMetric):
    def __init__(self):
        metric_path = __file__
        super(Add, self).__init__(metric_path)

    def compute(self, a1, a2):
        return a1 + a2
