from textnode import *
from htmlnode import HTMLNode

def main():
    dummy = HTMLNode("p", "Random info in tag", [], {"href":"www.google.com"})
    print(dummy.__repr__())

if __name__ == "__main__":
    main()



