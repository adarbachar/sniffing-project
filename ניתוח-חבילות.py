import pyshark
import matplotlib.pyplot as plt
import pandas as pd
from scapy.all import rdpcap

# Analyze network packets from different applications
# to understand the characteristics and behavior of each service

def extract_features(pcap_file):
    packets = rdpcap(pcap_file)
    sizes = [len(pkt) for pkt in packets]
    times = [pkt.time for pkt in packets]
    return pd.DataFrame({'size': sizes, 'time': times})

# Load packet data for various applications
apps = ['firefox', 'httpforever', 'rss', 'youtube', 'zoom']
data = {app: extract_features(f'{app}.pcap') for app in apps}

# Compare packet size distributions
plt.figure(figsize=(12, 6))
for app, df in data.items():
    plt.hist(df['size'], bins=100, alpha=0.5, label=app)
plt.xlabel('Packet Size (bytes)')
plt.ylabel('Frequency')
plt.title('Packet Size Distribution by Application')
plt.legend()
plt.show()

# Compare packet timing (inter-arrival times)
plt.figure(figsize=(12, 6))
for app, df in data.items():
    time_diff = df['time'].diff().dropna()
    plt.plot(time_diff, 'o', markersize=2, label=app)
plt.yscale('log')
plt.xlabel('Packet Index')
plt.ylabel('Time Between Packets (seconds)')
plt.title('Packet Timing by Application')
plt.legend()
plt.show()
