def moving_average(x, window_size):
    y = []

    for i in range(len(x)):
        if i < window_size:
            y.append(sum(x[:i+1]) / (i+1))
        else:
            y.append(sum(x[i-window_size+1:i+1]) / window_size)

    return y
