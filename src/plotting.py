import matplotlib.pyplot as plt

def plot_time(t, x_raw, x_filt, save_path):
    plt.plot(t, x_raw, label="raw")
    plt.plot(t, x_filt, label="filt")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
    plt.savefig(save_path)
    plt.close()
