import random
import matplotlib.pyplot as plt
import math
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n  * factorial(n-1)

def disting(list):
    global starting_p,destinations
    dist=0
    i=0
    for n in list:
        if i==0:
            dist+=math.dist([starting_p[0],starting_p[1]],[destinations[n-1][0],destinations[n-1][1]])
        elif i==len(list)-1:
            dist+=math.dist([destinations[n-1][0],destinations[n-1][1]],[starting_p[0],starting_p[1]])
        else:
            dist += math.dist([destinations[n-2][0],destinations[n-2][1]],[destinations[n-1][0],destinations[n-1][1]])
        i+=1
    return dist

nb_destinations = int(sys.argv[1])
destinations = []

for i in range(nb_destinations):
    destinations.append((random.randint(1,50),random.randint(1,50)))

nb_possibilities = factorial(nb_destinations-1)
plt.text(-19,65,f"Number of different paths = {nb_destinations-1}! = {nb_possibilities}")

starting_p = destinations[random.randint(0,nb_destinations-1)]
plt.plot(starting_p[0],starting_p[1],'o',color='black',markersize=10)
plt.text(starting_p[0],starting_p[1]-5,"Start",color='black',fontsize=8,horizontalalignment='center')
destinations.remove(starting_p)

i=1

paths = []
used = []
while len(paths) != nb_possibilities:
    path = random.sample(range(1,nb_destinations),nb_destinations-1)
    if path not in used:
        paths.append(path)
        used.append(path)
paths_with_dists = {}
thomas = 0
for n in paths:
    paths_with_dists[thomas] = (disting(n),n)
    thomas+=1

dists = []
paths = []

for n in paths_with_dists:
    dists.append(paths_with_dists[n][0])
    paths.append(paths_with_dists[n][1])

best_path = paths[dists.index(min(dists))]
best_dist = min(dists)
print(f"Best path is {best_path} with {best_dist}")

x=[starting_p[0]]
y=[starting_p[1]]


for n in best_path:
    x.append(destinations[n-1][0])
    y.append(destinations[n-1][1])

plt.plot(x,y,linestyle="solid",color="red")        

for x,y in destinations:
    plt.plot(x,y,'o',color='black')
    plt.text(x,y-5,str(i),fontsize=8)
    i+=1

plt.xlim(-20,70)
plt.ylim(-20,70)
plt.show()


