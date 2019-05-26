import numpy as np
import matplotlib.pyplot as plt


def f(x): return ((0.9)**(x)*(1)+(1-(0.9)**(x))*(x+1))/x

x=np.arange(2,20,1)
y1=f(x)

plt.plot(x,y1,'g^')
plt.axis([1, 20, 1/2, 1])
plt.title('Collective method with different times')
plt.xlabel('Times')
plt.ylabel('The ratio of expectation')
plt.xticks([2,4,6,8,10,12,14,16,18,20])
plt.yticks([1/2,3/4,1])


plt.show()
