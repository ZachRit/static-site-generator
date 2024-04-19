import os, shutil

def copy_directory(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        raise Exception(f"{source_dir} directory does not exist. Unable to copy files")
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    files = os.listdir(source_dir)
    for file in files:
        source_path = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        print(f"Copying file from {source_path} to {dest_path}")
        if os.path.isdir(source_path):
            copy_directory(source_path, dest_path)
        else:
            shutil.copy(source_path, dest_path)
