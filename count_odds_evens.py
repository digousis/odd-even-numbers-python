import csv
import numpy as np
import matplotlib.pyplot as plt

with open("datasets/numbers.csv") as f:
	reader = csv.reader(f, delimiter=",")
	num_list_of_lists = list(reader)
	
num_list = list()
	
for i in range(0, len(num_list_of_lists)):
	num_list.append(num_list_of_lists[i][0])
	
np_list = np.array(num_list)
np_list = np_list.astype(np.int)

odds = 0
evens = 0

for i in range(0, len(np_list)):
	if(np_list[i] % 2 == 0):
		evens = evens + 1
	if(np_list[i] % 2 == 1):
		odds = odds + 1
		
labels = ["Odds", "Evens"]
values = [odds, evens]

odds_prcntg = (odds / (odds + evens)) * 100
evens_prcntg = (evens / (odds + evens)) * 100

prcntg = [str(odds_prcntg), str(evens_prcntg)]

for i in range(0, 2):
	labels[i] = labels[i] + ": " + prcntg[i] + "%"

plt.pie(values, labels=labels)

plt.axis('equal')
plt.show()