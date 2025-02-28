import unittest
from extract import extract_title 


class TestExtract(unittest.TestCase):
    def test_extract_title(self):
        markdown = '# Test header 1!'
        title = extract_title(markdown)
        self.assertEqual(title, "Test header 1!")

        markdown = """


This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# This is an h1


* This is the first list item in a list block
* This is a list item
* This is another list item


"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is an h1")
