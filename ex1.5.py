import time
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def func_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        result = func_memo(n-1, memo) + func_memo(n-2, memo)
        memo[n] = result
        return result

def time_func(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return end - start

def plot_times(func):
    x = list(range(36))
    y = [time_func(func, n) for n in x]
    plt.plot(x, y)

if __name__ == '__main__':
    plt.title("Running time of the original and optimized code")
    plt.xlabel("Input size (n)")
    plt.ylabel("Running time (seconds)")
    plot_times(func)
    plot_times(func_memo)
    plt.legend(["Original", "Optimized"])
    plt.show()