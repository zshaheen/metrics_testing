import cdp_metric

class Sub(cdp_metric.CDPMetric):
    def __init__(self):
        metric_path = __file__
        super(Sub, self).__init__(metric_path)

    def compute(self, s1, s2):
        return s1 - s2
