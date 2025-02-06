import unittest
from htmlnode import HTMLNode 


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

    def test_props(self):
        node1 = HTMLNode(props={"href":"https://www.google.com", "target":"_blank",})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node1.__props_to_html__())
        

    def test_repr(self):
        node1 = HTMLNode("p", "Random info in tag", None, {"href":"www.google.com"})
        self.assertEqual("HTMLNode(tag=p, value=Random info in tag, children=None, props={'href': 'www.google.com'})", repr(node1))

