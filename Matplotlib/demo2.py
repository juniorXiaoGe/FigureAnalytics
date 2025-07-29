import matplotlib.pyplot as plt
import numpy as np
from sympy.printing.pretty.pretty_symbology import line_width

ary=np.array([1,10])
plt.plot(ary,linewidth=5)

plt.tick_params(axis='both',labelsize=30)

plt.show()