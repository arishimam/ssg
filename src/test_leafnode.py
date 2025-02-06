import unittest

from leafnode import LeafNode

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
        node1 = LeafNode("p") 
        with self.assertRaises(ValueError):
            node1.__to_html__() 
         
