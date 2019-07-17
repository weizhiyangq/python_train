import numpy as np
import math
import matplotlib.pyplot as plt


x=np.arange(-4,4,0.01)
y=[math.tanh(i) for i in x]
fig=plt.figure()
ax=plt.subplot()
plt.plot(x,y,'k')
plt.title('y=tanh(x)')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

