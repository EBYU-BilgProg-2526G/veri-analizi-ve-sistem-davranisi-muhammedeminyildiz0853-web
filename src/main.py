import numpy as np
import matplotlib.pyplot as plt

from signal_io import load_signal_csv
from signal_analysis import sampling_rate, basic_stats

def moving_average(x, n):
    y = []
    for i in range(len(x)):
        if i < n:
            y.append(np.mean(x[:i+1]))
        else:
            y.append(np.mean(x[i-n+1:i+1]))
    return np.array(y)

def main():
    t, x = load_signal_csv("signal.csv")

    fs = sampling_rate(t)
    stats = basic_stats(x)

    print("fs:", fs)
    for k in stats:
        print(k, ":", stats[k])

    y = moving_average(x, 5)

    plt.plot(t, x)
    plt.plot(t, y)
    plt.show()

if __name__ == "__main__":
    main()
