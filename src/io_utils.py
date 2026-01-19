import csv
import numpy as np

def load_signal_csv(path):
    t = []
    x = []

    with open(path, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            t.append(float(row[0]))
            x.append(float(row[1]))

    return np.array(t), np.array(x)
