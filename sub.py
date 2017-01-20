import cdp_metric

class Sub(cdp_metric.CDPMetric):
    def __init__(self, s1, s2):
        metric_path = __file__
        super(Sub, self).__init__(metric_path)
        self.s1 = s1
        self.s2 = s2

    def compute(self):
        return self.s1 - self.s2
