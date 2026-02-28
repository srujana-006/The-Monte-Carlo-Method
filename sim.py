import numpy as np
import matplotlib.pyplot as plt


lambda_rate = 4      # arrival rate (packets/sec)
mu_rate = 6          # service rate (packets/sec)
N = 50000            # number of packets


inter_arrival = np.random.exponential(1/lambda_rate, N)
arrival_times = np.cumsum(inter_arrival)


service_times = np.random.exponential(1/mu_rate, N)

start_times = np.zeros(N)
end_times = np.zeros(N)


for i in range(N):
    if i == 0:
        start_times[i] = arrival_times[i]
    else:
        start_times[i] = max(arrival_times[i], end_times[i-1])
    end_times[i] = start_times[i] + service_times[i]


delays = end_times - arrival_times

avg_delay_sim = np.mean(delays)
avg_delay_theory = 1 / (mu_rate - lambda_rate)
utilization = lambda_rate / mu_rate

print("Average Delay (Simulation):", avg_delay_sim)
print("Average Delay (Theory):", avg_delay_theory)
print("Server Utilization:", utilization)


plt.figure()
plt.hist(delays, bins=100)
plt.xlabel("Packet Delay")
plt.ylabel("Frequency")
plt.title("Delay Distribution (M/M/1)")
plt.show()
