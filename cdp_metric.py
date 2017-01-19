import abc
import sys
import logging


class CDPMetric():
    __metaclass__ = abc.ABCMeta

    def __init__(self, metric_path):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.metric_path = metric_path
        # print 'super is: '
        # print __file__

    def __call__(self):
        self.show_metric_information()
        return self.compute()

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
