import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics
import random
import csv
df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(mean)
print(std_deviation)
print(median)
print(mode)
fig = ff.create_distplot([data],["math scores"],show_hist = False)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)
mean = statistics.mean(mean_list)
print(mean)
fig = ff.create_distplot([mean_list],["student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = "lines",name = "Mean"))
fig.show()
