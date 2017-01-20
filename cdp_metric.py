import abc
import sys
import logging


class CDPMetric():
    __metaclass__ = abc.ABCMeta

    def __init__(self, metric_path):
        # Important variables
        # metric_path: printed when this metric is used. Let's users know which metric is being used
        # name: the name of the metric
        # _values: dictionary of the values. This allows for compound metrics. Explain more.
        #self.logger = logging.getLogger(__name__)
        #self.logger.setLevel(logging.DEBUG)
        self.metric_path = metric_path
        # get the filename from /path/to/filename.py
        name_with_py = self.metric_path.split('/')[-1]
        name = name_with_py.split('.')[0]
        self._values = {name: self.compute}

    def __call__(self):
        self.show_metric_information()
        if self._is_compound():
            # loop through and calculate all of the metrics
            for key, value in self._values.items():
                # replaces the function with the actual value
                self._values[key] = value()
            return self._values
        else:
            return self.compute()

    def __add__(self, other):
        class CompoundMetric(CDPMetric):
            def compute(self):
                pass
        compound_metric = CompoundMetric('a compound CDPMetric')
        self._merge_values_dict_into_first(compound_metric, self)
        self._merge_values_dict_into_first(compound_metric, other)
        return compound_metric

    def _is_compound(self):
        return len(self._values) > 1

    def _merge_values_dict_into_first(self, compound_metric, other_metric):
        """ Merges the _values dict of two objects of type CDPMetric
        into the first. """
        for key, value in other_metric._values.items():
            compound_metric._values[key] = value

    @abc.abstractmethod
    def compute(self):
        """ Compute the metric. """
        raise NotImplementedError()

    def show_metric_information(self):
        """ Displays information about this metric so that a user
        can easily identify what metrics are being used. """
        #self.logger.info(self.metric_path)
        #print sys.modules[__name__]
        #print __file__
        print 'Using metric: ' + self.metric_path
