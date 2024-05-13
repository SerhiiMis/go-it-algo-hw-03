import sys
import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    try:
        # We check if the target directory exist. If not, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # We go through all the elements in the source directory 
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)

            # If the elemetn is directory, call the function recursively
            if os.path.isdir(item_path):
                copy_files_recursive(item_path, dest_dir)

            # If the element is a file, copy it to the designated directory
            elif os.path.isfile(item_path):
                # We get the file extension
                _, extension = os.path.splitext(item)
                extension = extension[1:]  # We discard the dot at the begining of the extension
                # We create a subdirectory by the name of the extension, if it doesn't already exist
                extension_dir = os.path.join(dest_dir, extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                # Copy the file to the designated directory
                shutil.copy2(item_path, extension_dir)

    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    # Checcing for command lines arguments
    if len(sys.argv) < 2:
        print("Usage: python homework_3-1.py source_dir [destination_dir]")
        sys.exit(1)

    # Getting the paths to the source directory and the destination directory
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Calling a recursive function to copy files
    copy_files_recursive(source_dir, dest_dir)
