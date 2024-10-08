import os
import shutil

from blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type

def main():
    copy_source_contents_to_destination_dir(source_dir, destination_dir)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

main_path = os.path.dirname(os.path.abspath(__file__))
static_dir_path = os.path.join(main_path, '..', 'static')
public_dir_path = os.path.join(main_path, '..', 'public')

from_path = os.path.join(main_path, '..', 'content','index.md')
template_path = os.path.join(main_path, '..', 'template.html')
dest_path = os.path.join(main_path, '..', 'public')

source_dir = static_dir_path
destination_dir = public_dir_path

dir_path_content = os.path.join(main_path, '..', 'content')
dest_dir_path = os.path.join(main_path, '..', 'public')

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}\n")
    
    md_contents = open(from_path, "r").read()
    template = open(template_path, "r").read()
    
    node_contents = markdown_to_html_node(md_contents)
    html_contents = node_contents.to_html()
    html_title = extract_title(from_path)

    new_html = template.replace("{{ Title }}", html_title).replace("{{ Content }}", html_contents)

    os.makedirs(dest_path, exist_ok=True)
    parent_folder = os.path.dirname(from_path)

    if not parent_folder.endswith('content'):
        parent_folder_name = os.path.basename(parent_folder)
        parent_folder_path = os.path.join(dest_path, parent_folder_name)
        os.makedirs(parent_folder_path, exist_ok=True)
        file_path = os.path.join(parent_folder_path, 'index.html')
        with open(file_path, 'w') as file:
            file.write(new_html)
    else:
        file_path = os.path.join(dest_path, 'index.html')
        with open(file_path, 'w') as file:
            file.write(new_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        if os.path.isfile(dir_path_content):
            if dir_path_content.endswith('.md'):
                generate_page(dir_path_content, template_path, dest_dir_path)
        elif os.path.isdir(dir_path_content):
            dir_items = os.listdir(dir_path_content)
            for item in dir_items:
                item_path = os.path.join(dir_path_content, item)
                generate_pages_recursive(item_path, template_path, dest_dir_path)

def extract_title(from_path):
    md_contents = open(from_path, "r").read()
    md_blocks = markdown_to_blocks(md_contents)
    for block in md_blocks:
        if block_to_block_type(block) == "h1":
            return block.lstrip("# ")

if __name__ == "__main__":
    main()


