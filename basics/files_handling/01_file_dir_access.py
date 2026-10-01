import os
import glob

# Display the current working directory
print("Current working directory:", os.getcwd())

# Create a new directory named "new_directory"
new_directory_path = os.path.join(os.getcwd(), "new_directory")
if not os.path.exists(new_directory_path):
    os.mkdir(new_directory_path)
    print(f"Directory 'new_directory' created at: {new_directory_path}")

def date_time_format(timestamp):
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# display the contents of the current working directory
print("Contents of the current working directory:")
with os.scandir(os.getcwd()) as entries:
    for entry in entries:
        print("Name:", entry.name)
        info = entry.stat()
        print(f"creation time: {date_time_format(info.st_ctime)}, last modified time: {date_time_format(info.st_mtime)}, size: {info.st_size} bytes")

# display only directories in the current working directory
with os.scandir(os.getcwd()) as entries:
    for entry in entries:
        if entry.is_dir():
            print("dirname:", entry.name)

# display only files in the current working directory
with os.scandir(os.getcwd()) as entries:
    for entry in entries:
        if entry.is_file():
            print("filename:", entry.name)

# display all files in the current working directory with .py extension
# glob.glob() returns a list of file names matching the specified pattern.
print("All .py files in the current working directory:")
for file in glob.glob("*.py"):
    print(file)

# display all files matching .py extension in the current working directory and its subdirectories
# glob.iglob() returns an iterator which yields the file names matching the specified pattern.
print("All .py files in the current working directory and its subdirectories:")
for file in glob.iglob("**/*.py", recursive=True):
    print(file)

# os.walk() generates the file names in a directory tree by walking the tree.
# It yields a 3-tuple (dirpath, dirnames, filenames) for each directory in the tree.
# below is top-down approach, where the current directory is traversed first, then its subdirectories.
# for bottom-up approach, set the topdown parameter to False. # e.g. os.walk(os.getcwd(), topdown=False)
print("All files in the current working directory and its subdirectories using os.walk():")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("--------------------------------------------------")
    print(f"Current directory: {dirpath}")
    for dirname in dirnames:
        print(f"Directory: {os.path.join(dirpath, dirname)}")
    for filename in filenames:
        print(f"File: {os.path.join(dirpath, filename)}")


