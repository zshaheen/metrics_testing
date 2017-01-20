import cdp_metric

class Add(cdp_metric.CDPMetric):
    def __init__(self, a1, a2):
        metric_path = __file__
        super(Add, self).__init__(metric_path)
        self.a1 = a1
        self.a2 = a2

    def compute(self):
        return self.a1 + self.a2
