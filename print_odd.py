import csv
import numpy as np

with open("numbers.csv") as f:
	reader = csv.reader(f, delimiter=",")
	num_list = list(reader)
	
new_list = list()
	
for i in range(0, len(num_list)):
	new_list.append(num_list[i][0])
	
np_list = np.array(new_list)
np_list = np_list.astype(np.int)

for i in range(0, len(np_list)):
	if(np_list[i] % 2 == 1):
		print(np_list[i])
