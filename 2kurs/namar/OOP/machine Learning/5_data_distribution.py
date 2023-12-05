

# How Can we Get Big Data Sets? and show histogram
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 20)

print(x)
plt.hist(x, 5)
plt.show()
