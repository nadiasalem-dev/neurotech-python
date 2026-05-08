import math
import matplotlib.pyplot as plt
import random
data = []
spike_count = 0
threshold = 1.2
burst_count = 0
for i in range(200):
    wave = math.sin(i*.09)
    noise = random.uniform(-.02, .02)
    spike = 0
    if(random.random() < .1):
        spike = random.uniform(1.5, 3)
    if(random.randint(0,1) == 1):
        spike = -1 * spike
    value = wave + noise + spike
    data.append(value)
for i in range(1, len(data)-1):
    prev = data[i-1]
    cur = data[i]
    nextVal = data[i+1]
    if(abs(cur - prev) > threshold and abs(cur - nextVal) > threshold):
        spike_count += 1
    if((cur > 1 or cur < -1) and (prev > 1 or prev < -1) and (nextVal > 1 or nextVal < -1) ):
        burst_count += 1
for value in data:
    print(i)
plt.plot(data)
plt.title("Plot Random")
plt.show()
print(f"Spikes: {spike_count}, Bursts: {burst_count}")