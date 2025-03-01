import os
import shutil
from markdown_blocks import markdown_to_html_node
from extract import extract_title 
from htmlnode import * 


def file_copy(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    contents = os.listdir(source_dir)
    for c in contents:
        s_path = os.path.join(source_dir, c)
        t_path = os.path.join(target_dir, c)
        print(f" * {s_path} -> {t_path}")
        
        if os.path.isfile(s_path):
            shutil.copy(s_path, t_path)
        else:
            file_copy(s_path, t_path)

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open_store_file(from_path)
    template_file = open_store_file(template_path)
    
    html_node = markdown_to_html_node(markdown_file)
    html = html_node.__to_html__()

    title = extract_title(markdown_file)

    title_inserted = template_file.replace('{{ Title }}', title)
    content = title_inserted.replace('{{ Content }}', html)

    content = content.replace('href="/', f'href="{basepath}')
    content = content.replace('src="/', f'src="{basepath}')


    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    # Create new file by using write mode
    file = open(dest_path + "/index.html", 'w')
    file.write(content)
    file.close()


def open_store_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found at file path!")
        return None
    except Exception:
        print(f"An error occured {Exception}")
        return None
            

def generate_pages_recursive(basepath, source_dir, template_path, target_dir):

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    contents = os.listdir(source_dir)

    for c in contents:
        source_path = os.path.join(source_dir, c)
        # if c is a file, call generate page
        # else make recursive call
        if os.path.isfile(source_path):
            generate_page(basepath, source_path, template_path, target_dir)
        else:
            target_path = os.path.join(target_dir, c)
            generate_pages_recursive(basepath, source_path, template_path, target_path)

#generate_page('./content/index.md','./template.html', './public')

if __name__ == "__main__":
    source = "./static"
    target = "./public"
    file_copy(source, target)


