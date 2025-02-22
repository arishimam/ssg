import os
import shutil

# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
# It should first delete all the contents of the destination directory to ensure that the copy is clean.
# It should copy all files and subdirectories, nested files, etc.
# I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.

def file_copy(source_dir, target_dir):
    # delete contents of destination directory. /public
    # recreate empty public dir
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

    os.mkdir(target_dir)


    # Copy all files and subdirectories from static
    # List out everything in static
    # Iterate through
    # If something is a file, copy it to target

    contents = os.listdir(source_dir)
    for c in contents:
        s_path = source_dir + '/' + c
        t_path = target_dir + '/' + c
        
        if os.path.isfile(s_path):
            shutil.copy(s_path, t_path)
        else:
            # recursive call?
            file_copy(s_path, t_path)

    
    # if its a directory, check if the directory exists at target, if not then create it
    # then recursively call file copy ???
    

    # use os.listdir to list out static and then iterate through results and make recursive call from there
    # use os.isfile or os.isdir as we iterate through 

    # Log path of each copied file

# How to do this recursively ? What happens when I first access the src dir and how do I access?ggi
if __name__ == "__main__":
    source = "/Users/arish/workspace/github/arishimam/ssg/static"
    target = "/Users/arish/workspace/github/arishimam/ssg/public"

    file_copy(source, target)


