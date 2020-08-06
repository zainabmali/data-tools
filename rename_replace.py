import json
import os
import argparse

def update_filename(dir_path, old_text, new_text):
	'''Replace a word in the filename of all the files in a directory'''
	snr_dict = {}
	metadata_files = []
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			os.rename(dir_path + file, dir_path + file.replace(old_text, new_text))

def replace_within_files(dir_path, key_name, new_value):
	'''Update the same key, value pair in a directory of json files'''
	metadata_files = []
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			if file.endswith(".json"):
				metadata_files.append(os.path.join(root, file))

	for metadata_file in metadata_files:
		with open(metadata_file, 'r+') as f:
			metadata = json.load(f)
			for key, val in metadata.items():
				print(key, val)
				metadata[key_name] = new_value
			f.seek(0)
			json.dump(metadata, f, indent=2)
			f.truncate()
			f.close()

def main():
	dir_path = ''
	update_filename(dir_path, old_text='', new_text='')
	replace_within_files(dir_path, key_name='', new_value='')

if __name__ == '__main__':
	main()