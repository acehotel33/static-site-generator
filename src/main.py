import os
import shutil

def main():
    # print(os.path.exists(destination_dir))
    # print(f"Contents of source directory:\n{os.listdir(source_dir)}")
    # print(f"Contents of destination directory:\n{os.listdir(destination_dir)}")
    # delete_contents_of_dir(destination_dir)
    # print(f"Contents of destination directory:\n{os.listdir(destination_dir)}")
    copy_source_contents_to_destination_dir(source_dir, destination_dir)
    # print(f"Contents of destination directory:\n{os.listdir(destination_dir)}")

static_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')
public_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public')

source_dir = static_dir_path
destination_dir = public_dir_path

def delete_contents_of_dir(dir_path):
    if os.path.exists(dir_path):
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"The directory {directory_path} does not exist")

def copy_source_contents_to_destination_dir(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    if os.path.exists(source_path):
        if os.path.isfile(source_path) or os.path.islink(source_path):
            shutil.copy(source_path, destination_path)
        elif os.path.isdir(source_path):
            for file in os.listdir(source_path):
                file_source_path = os.path.join(source_path, file)
                file_destination_path = os.path.join(destination_path, file)

                if os.path.isdir(file_source_path):
                    copy_source_contents_to_destination_dir(file_source_path, file_destination_path)
                else:
                    shutil.copy(file_source_path, destination_path)
    else:
        print(f"One of two paths is invalid: {source_path} or {destination_path}")

main()


