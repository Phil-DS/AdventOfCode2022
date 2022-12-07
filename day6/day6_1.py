from data import data

packet_size = 14

for i in range(len(data)-packet_size):
    marker = data[i:i+packet_size]
    if len(set(marker)) == packet_size:
        print(i+packet_size)
        break
