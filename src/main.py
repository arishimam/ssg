from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    dummy = LeafNode("p", "Random info in tag", props={"href":"www.google.com"})
    print(dummy.__repr__())

if __name__ == "__main__":
    main()



