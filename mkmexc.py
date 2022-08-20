import pickle
import sys
with open(sys.argv[1], 'r') as file:
    data = file.read()
with open(sys.argv[1] + '.mexc', 'wb') as file:
    pickle.dump([data[i:i+1] for i in range(0, len(data), 1)], file)