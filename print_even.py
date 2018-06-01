import csv
import numpy as np

with open("numbers.csv") as f:
	reader = csv.reader(f, delimiter=",")
	num_list_of_lists = list(reader)
	
num_list = list()
	
for i in range(0, len(num_list_of_lists)):
	num_list.append(num_list_of_lists[i][0])
	
np_list = np.array(num_list)
np_list = np_list.astype(np.int)

for i in range(0, len(np_list)):
	if(np_list[i] % 2 == 0):
		print(np_list[i])
