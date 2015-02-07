from flask import Flask, Response
from common import get_filesystem
app = Flask(__name__)

filesystem = get_filesystem()

def find_item(path):
	# split path using /
	path = path.split('/')
	# start at root
	current_dir = filesystem.root()
	for item in path:
		for cloud_item in current_dir.list():
			# advance into the directory tree
			if cloud_item.name == item:
				current_dir = cloud_item
	return current_dir

@app.route('/list/', defaults={'path':''})
@app.route('/list/<path:path>')
def list(path):
	output = ''
	cloudfs_item = find_item(path)

	if cloudfs_item.type == 'file':
		# show file contents
		output = cloudfs_item.read()
	else:
		for dir_item in cloudfs_item.list():
			output += dir_item.name
			if dir_item.type == 'folder':
				output += '/'
			output += '\n'

	return Response(output, mimetype='text/plain')

@app.route('/clean')
def clean():
	deleted = ""
	for cloudfs_item in filesystem.root().list():
		# record name of deleted file
		deleted += "Deleting {}\n".format(cloudfs_item.name)
		# send to trash
		cloudfs_item.delete(force=True, commit=True)

	return Response(deleted or "nothing to delete", mimetype='text/plain')

if __name__ == '__main__':
	app.debug = True
	app.run()