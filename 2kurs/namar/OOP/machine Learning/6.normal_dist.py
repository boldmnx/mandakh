

import numpy
import matplotlib.pyplot as plt

# 4<5<6 хүртэл 19 тоо үүсгэхйг заасан бна
x = numpy.random.normal(5.0, 1.0, 19)

plt.hist(x, 9)  # 9ширхэг бар зурна гэж заажээ
plt.show()
