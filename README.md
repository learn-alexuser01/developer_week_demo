# Developer Week Demo Programs

Sample programs to demonstrate what CloudFS does best: make data accessible.

##Client
Setup: pip install cloudfs

To run: `python client.py <directory>`

Scans the provided directory and uploads the directory tree to the users' file system.

##Server
Setup: pip install cloudfs flask


To run: `python server.py`

Endpoints:

* `/list/<path>`: Lists the directory or file specified by the path.
* `/clean`: Moves the current contents of the filesystem to the trash.

Allows users to browse the files and directories created by the client over HTML

Presentation: http://slides.com/danieldrexler/devweekdeck

**Warning: Credentials in code are from a free account, the request limit might run out!
If it does, sign up at https://www.bitcasa.com to try it out.**
