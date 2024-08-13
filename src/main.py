import os

def main():
    # print(os.path.exists(destination_dir))
    print("Contents of source directory:")
    print(os.listdir(source_dir))
    print("Contents of destination directory:")
    print(os.listdir(destination_dir))
    delete_contents_of_dir(destination_dir)
    print(os.listdir(destination_dir))


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



main()


