# Purpose: caculate freq. of lexico-grammatical features in the AntTag and AntConc output 
# This script is for processing a list of excel files in corpus but return to just one output file with the whole dataset
# To run this script in Anaconda: python antcount.py --input_dir = input folder

import argparse
import os
import pandas
from pandas import DataFrame

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='Create merged spreadsheet')
parser.add_argument('--input_dir', action='store',dest='input_dir',default='')
parser.add_argument('--output_file', action='store',dest='output_file',default='')
args = parser.parse_args()

# Create a function to build data frame
def build_data_frame (filename):
	File = filename
	Data = pandas.read_excel(File)
	Data_Frame = pandas.DataFrame(Data)
	return (Data_Frame)

# Create a function to build data frame based on feature frequencies
def build_feature_counting_frame (Data_Frame):
	Data_Frame['Feature_Counting'] = Data_Frame.groupby('Filename')['Filename'].transform('count')
	Selected_Data_Frame = Data_Frame[['Filename', 'Feature_Counting']]
	Feature_Counting_Data_Frame = Selected_Data_Frame.drop_duplicates(subset='Filename', keep='first')
	return (Feature_Counting_Data_Frame)

# To-do: making this part a function and then write a loop to create data_frame 1, 2, 3 ... and add a function to merge them at once
for (root,dirs,filenames) in os.walk(args.input_dir):
	#print (root)
	#print (dirs)
	#print (filenames)

	for filename in filenames:
		if '.xlsx' in filename or '.xls' in filename:
			print("Processing: " + filename)
			filename_wo_ext = os.path.splitext(filename)[0] # Split x.xlsx to ['x', '.xlsx']
			Data_Frame = build_data_frame(os.path.join(root, filename)) # Send the right parameter to build_data_frame function: root + filename (folder\*.xlsx) 
			Feature_Counting_Data_Frame = build_feature_counting_frame(Data_Frame)
			Feature_Counting_Data_Frame = Feature_Counting_Data_Frame.rename(columns={'Feature_Counting': str(filename_wo_ext)})

			# Identify current working folder and create output folder and files
			cwd = os.getcwd()
			path = os.path.join(cwd, "dataset")
			if not os.path.exists(path):
				os.makedirs(path)
			Feature_Counting_Data_Frame.to_excel(os.path.join(path, filename), index=False)

print ('Done...')
