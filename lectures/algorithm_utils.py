import time


def time_function(func, params):
    """
    Returns the approximate run-time of a function, in milliseconds
    """
    start_time = time.time()
    result = func(*params)
    end_time = time.time()
    return end_time - start_time


def normalize(x):
    sum_vals = sum(x)
    return [val / sum_vals for val in x]


def plot_O_n(min_size, max_size):
    lengths = range(min_size, max_size)
    times = normalize(lengths)
    seaborn.lineplot(x="Length", y="O(n)", data=pandas.DataFrame({"Length": lengths, "O(n)": times}))
