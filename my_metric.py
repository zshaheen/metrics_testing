import cdp_metric

class MyMetric(cdp_metric.CDPMetric):
    def __init__(self, d1, d2):
        metric_path = __file__
        super(MyMetric, self).__init__(metric_path)
        self.d1 = d1
        self.d2 = d2

    def compute(self):
        return self.d1 + self.d2
