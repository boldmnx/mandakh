import numpy
import math

ages = numpy.random.uniform(0, 100, 30).astype(int)

# What is the age that 90% of the people are younger than?
# 75 huviig n yamar nasniihan ezelj bn ve


n = numpy.percentile(ages, 20)
print(ages)
print(n)
