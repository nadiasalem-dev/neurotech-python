import math
import matplotlib.pyplot as plt
import random
data = []
spike_count = 0
threshold = 1.2
burst_count = 0
sensitivity = 2.5
differences = []
spike_indexes = []
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
mean = sum(data)/len(data)
for i in range(len(data)):
    differences.append(pow(data[i]-mean, 2))
variance = sum(differences)/len(differences)
standard_deviation = math.sqrt(variance)
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard deviation: {standard_deviation}")
detected_labels = [0] * len(data)
for i in range(0, len(data)):
    if(abs(data[i] - mean) > sensitivity * standard_deviation):
        spike_count += 1
        detected_labels[i] = 1
        spike_indexes.append(i) 
for i in range(0, len(spike_indexes)-2):
    if(spike_indexes[i+2] <= spike_indexes[i]+20):
        burst_count+=1
        print(f"burst indexes: {spike_indexes[i]}, {spike_indexes[i+1]}, {spike_indexes[i+2]}")
plt.plot(data)
plt.title("Plot Random")
plt.show()
print(f"Spikes: {spike_count}, Bursts: {burst_count}")
for i in range(0, len(spike_indexes)):
    print(spike_indexes[i])