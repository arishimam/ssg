import unittest
from textnode import TextNode, TextType

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
        
if __name__ == "__main__":
    unittest.main()



