import os   
import shutil
from static_to_public import file_copy, generate_pages_recursive

def main():
    source_static = './static' 
    target = './public'

    if os.path.exists(target):
        shutil.rmtree(target)

    file_copy(source_static, target)

    #source_page = './content/index.md'
    source_public = './content'
    # generate_page(source_page, 'template.html', target)
    generate_pages_recursive(source_public, 'template.html', target)
    

if __name__ == "__main__":
    main()



