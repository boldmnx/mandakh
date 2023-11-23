# Machine learning have three value
import numpy
from scipy import stats
speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
nMean = numpy.mean(speed)  # average
nMedian = numpy.median(speed)  # middle
nMode = stats.mode(speed)  # common
print(nMode)
