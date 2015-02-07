from os.path import join, split
import os
import sys

from common import get_filesystem

filesystem = get_filesystem()

folders = {}

def create_folder(cloudfs_folder, new_folder_name):
	new_folder_name = new_folder_name.strip('/')
	print 'creating Folder "{}" in {}'.format(new_folder_name, cloudfs_folder.name)
	return cloudfs_folder.create_folder(new_folder_name)

def create_file(cloudfs_folder, local_path):
	print 'uploading File: {}'.format(local_path)
	cloudfs_folder.upload(local_path)

def walk(directory):
	(path, root_name) = split(directory)
	# handle trailing /
	if root_name == '':
		(path, root_name) = split(path)
	
	if path != '':
		os.chdir(path)
	# create root folder
	folders[root_name] = create_folder(filesystem.root(), root_name)

	# walk command
	for current_directory, sub_directory_names, file_names in os.walk(root_name):
		
		# skip paths with hidden folders
		if current_directory.find('.') >0:
			continue

		# get cloudfs folder out of dictionary
	 	cloudfs_folder = folders[current_directory]

	 	# create folders so we'll have them when we want them
	 	for sub_dir in sub_directory_names:
	 		# don't create hidden directories
	 		if sub_dir[0] != '.':
		 		expected_path = join(current_directory, sub_dir)
		 		folders[expected_path] = create_folder(cloudfs_folder, sub_dir)
	 	
	 	# upload files in this directory
	 	for filename in file_names:
	 		path = join(current_directory, filename)
	 		create_file(cloudfs_folder, path)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'usage: python client.py <directory>'
	else:
		walk(sys.argv[1])