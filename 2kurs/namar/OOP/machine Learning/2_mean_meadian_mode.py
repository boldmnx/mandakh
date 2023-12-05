# Machine learning have three value
import numpy
import math
from scipy import stats


speed = numpy.random.uniform(50, 100, 9).astype(int)

print(speed)

meanSpeed = math.floor(numpy.mean(speed))  # average
medianSpeed = math.floor(numpy.median(speed))  # middle
modeSpeed = stats.mode(speed)  # common


print(f'meanSpeed {meanSpeed}')
print(f'medianSpeed {medianSpeed}')
print(f'modeSpeed {modeSpeed}')
