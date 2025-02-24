from static_to_public import file_copy 
import os   

def main():
    source = './static' 
    target = './public'
    file_copy(source, target)

if __name__ == "__main__":
    main()



