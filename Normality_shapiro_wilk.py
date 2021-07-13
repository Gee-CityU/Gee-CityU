import argparse
import numpy
import os
import pandas
import scipy
from pandas import DataFrame
from scipy.stats import shapiro

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='Run Shapiro-Wilk Test')
parser.add_argument('--input_file', action='store',dest='input_file',default='')
#parser.add_argument('--output_file', action='store',dest='output_file',default='')
args = parser.parse_args()

# Create a function to build data frame
def build_data_frame (CSVfile):
	data = pandas.read_csv(CSVfile)
	data_frame = pandas.DataFrame(data)
	return (data_frame)

# Create a function to run Shapiro-Wilk Test
def run_shapiro (Data):
    stat, p = shapiro(Data)
    return('Statistics=%.3f, p=%.3f' % (stat, p))

# Start the main program here
dataframe = build_data_frame(args.input_file)
selected_dataframe = dataframe[['ADJ', 'APP', 'NN', 'NOM', 'PPOF', 'PPOTHER', 'M1', 'M1S1', 'M1S2', 'M2', 'M2S1', 'M2S2', 'M3', 'M3S1', 'M4']]
#print(selected_dataframe)

print ('Running a Shapiro-Wilk Test...')
# Iterate column by column, build a data list based on the values in each column
for (column_name, column_data) in selected_dataframe.iteritems():
	#print('column_name: ', column_name)
	#print('column_data: ', column_data.values)
	normality = run_shapiro(column_data.values)
	print(normality)

print('Done.')
								