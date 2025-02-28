import os   
import shutil
from static_to_public import file_copy, generate_page 

def main():
    source = './static' 
    target = './public'

    if os.path.exists(target):
        shutil.rmtree(target)

    file_copy(source, target)

    source_page = './content/index.md'
    generate_page(source_page, 'template.html', target)

if __name__ == "__main__":
    main()



