# Purpose: make all lines in PDF-converted plain text files in a nice superline format
# Use: (1) run character normailizaiton files (e.g., normed_1, normed_2); (2) run this script to clean the file format and make it a superline for analysis

import argparse
import os
import re

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='mark headers')
parser.add_argument('--input_dir', action='store',dest='input_dir',default='')
args = parser.parse_args()

# To-do: making this part a function and then write a loop to create data_frame 1, 2, 3 ... and add a function to merge them at once
for (root,dirs,filenames) in os.walk(args.input_dir):
	for filename in filenames:
		if '.txt' in filename or '.TXT' in filename:
			print("Processing: " + filename)
			filename_wo_ext = os.path.splitext(filename)[0] # Split x.xlsx to ['x', '.txt']
			input_file = open (os.path.join(root, filename),'r') # Send the right parameter to open function: root + filename (folder\*.xlsx) 
			text = input_file.read()
			new_text = re.sub(r'(\bIntroduction\b|\bIntroduction:\b)', r'\n<INTRODUCTION>\n', text) # remove page number
			new_text = re.sub(r'(\bProcedures\b|\bProcedures:\b)', r'\n<PROCEDURES>\n', new_text)
			new_text = re.sub(r'(\bResults\b|\bResults:\b)', r'\n<RESULTS>\n', new_text)
			new_text = re.sub(r'(\bDiscussion\b|\bDiscussion:\b)', r'\n<DISCUSSION>\n', new_text)
			new_text = re.sub(r'(\bConclusion\b|\bConclusion:\b)', r'\n<CONCLUSION>\n', new_text)
			new_text = re.sub(r'(\bReferences\b|\bReferences:\b)', r'\n<REFERENCES>\n', new_text)
			new_text = re.sub(r'(\bAcknowledgement\b|bAcknowledgement:\b)', r'\n<<<ACKNOWLEDGEMENT>>>\n', new_text)
			print ('>>>>> header added')
			
			# Identify current working folder and create output folder and files
			cwd = os.getcwd()
			path = os.path.join(cwd, "markheader")
			if not os.path.exists(path):
				os.makedirs(path)
			output_file = open(os.path.join(path, filename),"w")
			print("producing the outputfile...")
			output_file.write(new_text)
			output_file.close()

print ('Done...')