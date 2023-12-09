# Machine learning have three value


from scipy import stats
import numpy

arr = [77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111]
print(numpy.mean(arr))    # output: 89 is average
print(numpy.median(arr))  # output: 87 is middle
print(stats.mode(arr))    # output: 86 is common


speed = numpy.random.uniform(50, 100, 9).astype(int)

# print(speed)

# meanSpeed = math.floor(numpy.mean(speed))  # average
# medianSpeed = math.floor(numpy.median(speed))  # middle
# modeSpeed = stats.mode(speed)  # common


# print(f'meanSpeed {meanSpeed}')
# print(f'medianSpeed {medianSpeed}')
# print(f'modeSpeed {modeSpeed}')
