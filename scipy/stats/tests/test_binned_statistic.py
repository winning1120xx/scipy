import numpy as np
from numpy.testing import assert_array_almost_equal
from scipy.stats import \
    binned_statistic, binned_statistic_2d, binned_statistic_dd

class TestBinnedStatistic(object):

    @classmethod
    def setup_class(cls):
        np.random.seed(9865)
        cls.x = np.random.random(100)
        cls.y = np.random.random(100)
        cls.v = np.random.random(100)
        cls.X = np.random.random((100, 3))

    def test_1d_count(self):
        x = self.x
        v = self.v

        count1, edges1 = binned_statistic(x, v, 'count', bins=10)
        count2, edges2 = np.histogram(x, bins=10)

        assert_array_almost_equal(count1, count2)
        assert_array_almost_equal(edges1, edges2)


    def test_1d_sum(self):
        x = self.x
        v = self.v

        sum1, edges1 = binned_statistic(x, v, 'sum', bins=10)
        sum2, edges2 = np.histogram(x, bins=10, weights=v)

        assert_array_almost_equal(sum1, sum2)
        assert_array_almost_equal(edges1, edges2)


    def test_1d_mean(self):
        x = self.x
        v = self.v

        stat1, edges1 = binned_statistic(x, v, 'mean', bins=10)
        stat2, edges2 = binned_statistic(x, v, np.mean, bins=10)

        assert_array_almost_equal(stat1, stat2)
        assert_array_almost_equal(edges1, edges2)


    def test_1d_median(self):
        x = self.x
        v = self.v

        stat1, edges1 = binned_statistic(x, v, 'median', bins=10)
        stat2, edges2 = binned_statistic(x, v, np.median, bins=10)

        assert_array_almost_equal(stat1, stat2)
        assert_array_almost_equal(edges1, edges2)


    def test_2d_count(self):
        x = self.x
        y = self.y
        v = self.v

        count1, binx1, biny1 = binned_statistic_2d(x, y, v, 'count', bins=5)
        count2, binx2, biny2 = np.histogram2d(x, y, bins=5)

        assert_array_almost_equal(count1, count2)
        assert_array_almost_equal(binx1, binx2)
        assert_array_almost_equal(biny1, biny2)


    def test_2d_sum(self):
        x = self.x
        y = self.y
        v = self.v

        sum1, binx1, biny1 = binned_statistic_2d(x, y, v, 'sum', bins=5)
        sum2, binx2, biny2 = np.histogram2d(x, y, bins=5, weights=v)

        assert_array_almost_equal(sum1, sum2)
        assert_array_almost_equal(binx1, binx2)
        assert_array_almost_equal(biny1, biny2)


    def test_2d_mean(self):
        x = self.x
        y = self.y
        v = self.v

        stat1, binx1, biny1 = binned_statistic_2d(x, y, v, 'mean', bins=5)
        stat2, binx2, biny2 = binned_statistic_2d(x, y, v, np.mean, bins=5)

        assert_array_almost_equal(stat1, stat2)
        assert_array_almost_equal(binx1, binx2)
        assert_array_almost_equal(biny1, biny2)


    def test_2d_median(self):
        x = self.x
        y = self.y
        v = self.v

        stat1, binx1, biny1 = binned_statistic_2d(x, y, v, 'median', bins=5)
        stat2, binx2, biny2 = binned_statistic_2d(x, y, v, np.median, bins=5)

        assert_array_almost_equal(stat1, stat2)
        assert_array_almost_equal(binx1, binx2)
        assert_array_almost_equal(biny1, biny2)


    def test_dd_count(self):
        X = self.X
        v = self.v

        count1, edges1 = binned_statistic_dd(X, v, 'count', bins=3)
        count2, edges2 = np.histogramdd(X, bins=3)

        assert_array_almost_equal(count1, count2)
        assert_array_almost_equal(edges1, edges2)


    def test_dd_sum(self):
        print "dd_sum"
        X = self.X
        v = self.v

        sum1, edges1 = binned_statistic_dd(X, v, 'sum', bins=3)
        sum2, edges2 = np.histogramdd(X, bins=3, weights=v)

        assert_array_almost_equal(sum1, sum2)
        assert_array_almost_equal(edges1, edges2)


    def test_dd_mean(self):
        X = self.X
        v = self.v

        stat1, edges1 = binned_statistic_dd(X, v, 'mean', bins=3)
        stat2, edges2 = binned_statistic_dd(X, v, np.mean, bins=3)

        assert_array_almost_equal(stat1, stat2)
        assert_array_almost_equal(edges1, edges2)


    def test_dd_median(self):
        X = self.X
        v = self.v

        stat1, edges1 = binned_statistic_dd(X, v, 'median', bins=3)
        stat2, edges2 = binned_statistic_dd(X, v, np.median, bins=3)

        assert_array_almost_equal(stat1, stat2)
        assert_array_almost_equal(edges1, edges2)
