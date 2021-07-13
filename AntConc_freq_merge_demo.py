# Purpose: merge all excel files in a directory to create a masterdataset
# This script is for processing a list of excel dataset and then return to just one output file with the whole dataset
# To run this script in Anaconda: python antcount.py --input_dir = input --output = master_dataset.csv

import argparse
import os
import pandas
import glob
from pandas import DataFrame

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='Create merged spreadsheet')
parser.add_argument('--input_dir', action='store',dest='input_dir',default='')
parser.add_argument('--output_file', action='store',dest='output_file',default='')
args = parser.parse_args()

#Master_Data_Frame = pandas.concat([pandas.read_excel(f).set_index('Filename') for f in glob.glob('*.xlsx')],axis=1).reset_index()
#Master_Data_Frame.to_excel(args.output_file, index=False)

for (root,dirs,filenames) in os.walk(args.input_dir):
    Master_Data_Frame = pandas.concat([pandas.read_excel(os.path.join(args.input_dir, filename)).set_index('Filename') for filename in filenames],axis=1).reset_index()
    Master_Data_Frame.to_excel(args.output_file, index=False)
print('Done...')


