import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_eq2(self):
        node1 = HTMLNode("p","random info", props={"href":"https://www.google.com", "target":"_blank",})
        node2 = HTMLNode("p","random info", props={"href":"https://www.google.com", "target":"_blank",})
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode("p","random info", props={"href":"https://www.google.com", "target":"_blank",})
        node2 = HTMLNode("p","random info")
        self.assertNotEqual(node1, node2)

    def test_values(self):
        node = HTMLNode(
            "div",
            "im just taking space",
            None,
            None
        )
        self.assertEqual("div", node.tag)
        self.assertEqual("im just taking space", node.value)
        self.assertEqual(None, node.children)
        self.assertEqual(None, node.props)

    def test_props(self):
        node1 = HTMLNode(
            "div",
            "Hello there!",
            None,
            {"href":"https://www.google.com", "target":"_blank",}
        )
        self.assertEqual(' href="https://www.google.com" target="_blank"', node1.__props_to_html__())

    def test_repr(self):
        node1 = HTMLNode("p", "Random info in tag", None, {"href":"www.google.com"})
        self.assertEqual("HTMLNode(tag=p, value=Random info in tag, children=None, props={'href': 'www.google.com'})", repr(node1))

        
class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node1 = LeafNode("p","Random info.") 
        self.assertEqual("<p>Random info.</p>", node1.__to_html__())

    def test_anchor_tag(self):
        node1 = LeafNode("a","Click here!", {"href":"www.google.com"}) 
        self.assertEqual("<a href=\"www.google.com\">Click here!</a>", node1.__to_html__())
        
    def test_multi_anchor_tag(self):
        node1 = LeafNode("a","Click here!", {"href":"www.google.com","title":"_blank",}) 
        self.assertEqual("<a href=\"www.google.com\" title=\"_blank\">Click here!</a>", node1.__to_html__())

    def test_no_val(self):
        node1 = LeafNode("p", None) 
        with self.assertRaises(ValueError):
            node1.__to_html__() 
         

class TestParentNode(unittest.TestCase):
    def test_recursion(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.__to_html__(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_nested_parent(self):
        node = ParentNode(
            "p",
            [
                ParentNode("b", [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                ]),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.__to_html__(), 
            "<p><b>Normal text<i>italic text</i></b>Normal text</p>"
        )
    def test_child(self):
        childnode = LeafNode("p", "im a child")
        parentnode = ParentNode("div",[childnode])

        self.assertEqual(
            parentnode.__to_html__(), 
            "<div><p>im a child</p></div>"
        )
    def test_grandchild(self):
        grandchildnode = LeafNode("b", "im a grandchild")
        childnode = ParentNode("p",[grandchildnode])
        parentnode = ParentNode("div",[childnode])

        self.assertEqual(
            parentnode.__to_html__(), 
            "<div><p><b>im a grandchild</b></p></div>"
        )





if __name__ == "__main__":
    unittest.main()
