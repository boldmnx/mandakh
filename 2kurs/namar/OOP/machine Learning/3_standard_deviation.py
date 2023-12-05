import numpy
import math

arr1 = numpy.random.uniform(0, 9, 9).astype(int)
stdArr1 = math.floor(numpy.std(arr1))
print(arr1)
print(f'standard devition: {stdArr1}')
