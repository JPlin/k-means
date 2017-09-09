import random as random
from clustering import clustering
from Point import Point
import csv

geo_locs = []

#read the fountains location from the csv input file and store each fountain location as a Poing object
f = open('points.csv','r')
reader = csv.reader(f,delimiter=",")
for line in reader:
	loc_ = Point(float(line[0]),float(line[1]))
	geo_locs.append(loc_)

print("num of points",loc_)
cluster = clustering(geo_locs , 8 )
flag = cluster.k_means(True)
if flag == -1:
	print("Error in data")
else:
	print("clustering result:")
	cluster.print_clusters(cluster.clusters)