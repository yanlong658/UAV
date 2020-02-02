import numpy as np
import pylab as plt

time_stamp = []
num_list = []
receve_list= []

for t in range(0,46,1):
    d = (2*t) + (t**2)
    num_list += [d]
    receve_list +=[d]
    time_stamp += [t]

## 製造數據
for i in range(0,46,1):
    receve_list[i] = round(num_list[i] + np.random.normal(0, 5),5)
print(num_list)
print(receve_list)

plt.figure(figsize=(6,8))
plt.subplot(411)
plt.title('The Original Signal')
plt.plot(time_stamp[0:46],num_list[0:46])

plt.title('Noise Signal')
plt.subplot(412)
plt.plot(time_stamp[0:46],receve_list[0:46])

plt.show()
plt.tight_layout()
