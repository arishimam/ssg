from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    t = text_node.text_type

    if t == TextType.NORMAL:
        return LeafNode(None, self.text)
    elif t == TextType.BOLD:
        return LeafNode("b", self.text)
    elif t == TextType.ITALIC:
        return LeafNode("i", self.text)
    elif t == TextType.CODE:
        return LeafNode("code", self.text)
    elif t == TextType.LINK:
        return LeafNode("a", self.text, {"href":self.url})
    elif t == TextType.IMAGE: 
        return LeafNode("img", None, {"src":self.url,"alt":self.text} )
    else:
        raise ValueError(f"Invalid text type {t}")
