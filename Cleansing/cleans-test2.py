import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("..\DataSET\live.csv", "r")
taxi_list = list(csv.reader(f))

taxi = np.array(taxi_list)