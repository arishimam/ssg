import os   
import shutil
import sys
from static_to_public import file_copy, generate_pages_recursive

def main():

    basepath = '/'

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    source_static = './static' 
    target = './docs'

    if os.path.exists(target):
        shutil.rmtree(target)

    file_copy(source_static, target)

    source_docs = './content'
    generate_pages_recursive(basepath, source_docs, 'template.html', target)
    

if __name__ == "__main__":
    main()



