import plotly.figure_factory as ff
import statistics as stat
import random
import pandas as pd

def sample(data, a, b):
    f = []
    for i in range(a):
        l = []
        for i in range(b):
            l.append(random.choice(data))
        f.append(stat.mean(l))
    return f

def printMMMSD(data):
    mean = stat.mean(data)
    median = stat.median(data)
    mode = stat.mode(data)
    sd = stat.stdev(data)
    print("mean:   ", mean, "\nmedian: ", median, "\nmode:   ", mode, "\nstdev:  ", sd)

d0 = pd.read_csv("data.csv")
nums0 = d0["reading_time"].tolist()

d1 = pd.read_csv("medium_data.csv")
nums1 = d1["reading_time"].tolist()

s0 = sample(nums0, 100, 30)

m0 = stat.mean(s0)
m1 = stat.mean(nums1)

s = stat.stdev(s0)

z = (m1 - m0) / s

print(z)