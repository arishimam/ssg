import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node1 = TextNode("This is a text node", TextType.BOLD) 
        node2 = TextNode("This is a text node", TextType.BOLD) 
        self.assertEqual(node1, node2)

        
    def test_eq2(self):
        node3 = TextNode("This is a text node", TextType.ITALIC) 
        node4 = TextNode("This is a text node", TextType.ITALIC) 
        self.assertEqual(node3, node4)

    def test_eq3(self):
        node5 = TextNode("Powder.com", TextType.LINK, "https://www.powder.com") 
        node6 = TextNode("Powder.com", TextType.LINK, "https://www.powder.com") 
        self.assertEqual(node5, node6)

    def test_not_eq1(self):
        node1 = TextNode("This is a node", TextType.BOLD) 
        node2 = TextNode("This is a text node", TextType.BOLD) 
        self.assertNotEqual(node1, node2)

    def test_not_eq1(self):
        node3 = TextNode("This is a text node", TextType.BOLD) 
        node4 = TextNode("This is a text node", TextType.ITALIC) 
        self.assertNotEqual(node3, node4)

    def test_not_eq1(self):
        node5 = TextNode("Powder.com", TextType.LINK, "https://powder.com") 
        node6 = TextNode("Powder.com", TextType.LINK, "https://www.powder.com") 
        self.assertNotEqual(node5, node6)

    def test_repr(self):
        node = TextNode("Powder.com", TextType.LINK, "https://www.powder.com") 
        self.assertEqual("TextNode(Powder.com, link, https://www.powder.com)", repr(node))

            
class TestTextNodeToHTMLNode:
    def test_text_to_html(self):
        node = TextNode("Powder.com", TextType.NORMAL) 
        self.assertEqual(text_node_to_html_node(node), LeafNode(None,"Powder.com"))

        node = TextNode("Powder.com", TextType.BOLD) 
        self.assertEqual(text_node_to_html_node(node), LeafNode("b","Powder.com"))

        node = TextNode("Powder.com", TextType.ITALIC) 
        self.assertEqual(text_node_to_html_node(node), LeafNode("i","Powder.com"))

        node = TextNode("Powder.com", TextType.CODE) 
        self.assertEqual(text_node_to_html_node(node), LeafNode("code","Powder.com"))

        node = TextNode("Powder.com", TextType.LINK, "https://www.powder.com") 
        self.assertEqual(text_node_to_html_node(node),LeafNode("a","Powder.com",{"href":"https://www.powder.com"}))

        node = TextNode("Powder.com", TextType.IMAGE, "https://www.powder.com") 
        self.assertEqual(text_node_to_html_node(node), LeafNode("img",None,{"src":"https://www.powder.com", "alt":"Powder.com"}))

    def test_err_text_to_html(self):
        with self.assertRaises(AttributeError):
            node = TextNode("Powder.com", TextType.BIG) 

        
if __name__ == "__main__":
    unittest.main()



