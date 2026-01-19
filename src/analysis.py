
import numpy as np

def sampling_rate(t):
    dt = t[1] - t[0]
    return 1 / dt


def basic_stats(x):
    return {
        "mean": np.mean(x),
        "std": np.std(x),
        "rms": np.sqrt(np.mean(x**2)),
        "min": np.min(x),
        "max": np.max(x)
    }
