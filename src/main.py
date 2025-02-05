from textnode import *

def main():
    dummy = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(dummy.__repr__())

if __name__ == "__main__":
    main()



