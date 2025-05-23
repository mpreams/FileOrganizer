import os
import shutil
from file_extensions import extensions
        

source_path = "/Users/matthewreams/Downloads/"  # Replace with your folder path

file_names = os.listdir(source_path)
for name in file_names:
    split_name = os.path.splitext(name)
    if split_name[1] in extensions:
        source = os.path.join(source_path, name)
        destination = os.path.join(source_path, extensions[split_name[1]], name)
        destination_path = os.path.join(source_path, extensions[split_name[1]])
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        shutil.move(source, destination)



