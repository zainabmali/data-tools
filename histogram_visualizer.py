import os
from matplotlib import pyplot as plt
import numpy as np
import decimal

def histogram_two_data_sets(list_1, list_2, 
	list_1_name, list_2_name, x_label, dir_name):
	'''Visualize 2 distributions on one histogram and print relevant statistics.

	Args:
		list_1:data set 1
		list_2: data set 2
		list_1_name: description of data set 1
		list_2_name: description of data set 2
		x_label: label for x-axis
		dir_name: directory name where plots will be saved

	Returns:
		mean 1
		mean 2
		standard deviation 1
		standard deviation 2
		z statistic
	'''

	print('Number of values in ' + list_1_name + ' histogram: ' 
		+ str(len(list_1)))
	print('Number of values in ' + list_2_name + ' histogram: ' 
		+ str(len(list_2)))
	plt.style.use('fivethirtyeight')
	
	plt.hist(list_1, bins=5, edgecolor='black', 
		density=True, alpha=0.6, log=False, label=list_1_name)
	plt.hist(list_2, bins=5, edgecolor='black', 
		density=True, alpha=0.6, log=False, label=list_2_name)
	plt.legend()
	plt.title(list_1_name + ', ' + list_2_name)
	plt.xlabel(x_label)
	
	mean_1 = float(round(np.mean(list_1), 3))
	print(list_1_name + ' scores mean: ' + str(mean_1))
	plt.axvline(mean_1, color='g', linestyle='dashed', linewidth=1)
	
	mean_2 = float(round(np.mean(list_2), 3))
	print(list_2_name + ' scores mean: ' + str(mean_2))
	plt.axvline(mean_2, color='m', linestyle='dashed', linewidth=1)

	mean_difference = round(abs(mean_1 - mean_2), 3)
	print('Mean difference: ' + str(mean_difference))

	std_1 = float(round(np.std(list_1), 3))
	print(list_1_name + ' standard deviation: ' + str(std_1))
	
	std_2 = float(round(np.std(list_2), 3))
	print(list_2_name + ' standard deviation: ' + str(std_2))

	z_stat = z_test(list_1, list_2)
	z_stat = abs(float(round(z_stat,3)))
	print('z-statistic: ' + str(z_stat))
	print('\n')
	
	plt.tight_layout()
	plt.savefig(dir_name + z_stat + "_" + 'hist', bbox_inches='tight')
	plt.show()
	return mean_1, mean_2, std_1, std_2, z_stat
	

def z_test(x_1, x_2):
	'''Compute z-statistic for 2 distributions.

	Z-test to compare two distributions as described here:
	http://homework.uoregon.edu/pub/class/es202/ztest.html

	Args:
		x_1: Distribution 1.
		x_2: Distribution 2.

	Returns:
		z statistic.
	'''
	x_bar_1 = np.mean(x_1)
	x_bar_2 = np.mean(x_2)
	std_1 = np.std(x_1)
	std_2 = np.std(x_2)
	sigma_1 = std_1/np.sqrt(len(x_1))
	sigma_2 = std_2/np.sqrt(len(x_2))
	z = (x_bar_1 - x_bar_2)/np.sqrt((sigma_1**2) + (sigma_2**2))
	return z

def main():

	list_1 = ''
	list_2 = ''

	histogram_two_data_sets(list_1, list_2, 
	list_1_name, list_2_name, x_label, dir_name)


if __name__ == '__main__':
	main()