import os
import shutil
from file_extensions import extensions
        
def organize_files(source_path):
    """
    Organizes files in the specified directory by moving them into subdirectories based on their file extensions.
    """

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

if __name__ == "__main__":
    organize_files("/Users/matthewreams/Downloads/")

