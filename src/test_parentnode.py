import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode
from parentnode import ParentNode

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
