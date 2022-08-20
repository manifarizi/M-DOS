import pickle
import sys
with open(sys.argv[1], 'r') as file:
    data = file.read()
with open(sys.argv[1] + '.mexc', 'wb') as file:
    pickle.dump(data, file)