import unittest
from split_blocks import *

class TestSplitBlocks(unittest.TestCase):
    def test_split_markdown_to_blocks(self):
        markdown = """

# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item


"""
        blocks = markdown_to_blocks(markdown)

        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ]
        )

    def test_block_type_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(
            block_to_block_type(block),
            "paragraph"
        )


    def test_block_type_header(self):
        block = "# This is a heading"
        self.assertEqual(
            block_to_block_type(block),
            "heading"
        )

        block2 = "#### This is also a heading"
        self.assertEqual(
            block_to_block_type(block2),
            "heading"
        )

    def test_block_type_code(self):
        block = "```This\n is a code\n block ```"
        self.assertEqual(
            block_to_block_type(block),
            "code"
        )

    def test_block_type_quote(self):
        block = ">This is a quote block\n>More\n>last bit. "
        self.assertEqual(
            block_to_block_type(block),
            "quote"
        )

    def test_block_type_unordered(self):
        block = "- This is an unordered list block\n- Second "
        self.assertEqual(
            block_to_block_type(block),
            "unordered_list"
        )

        block2 = "* This is an unordered list block "
        self.assertEqual(
            block_to_block_type(block2),
            "unordered_list"
        )

    def test_block_type_unordered_fail(self):
        block = "- This is an unordered list block\nSecond "
        self.assertEqual(
            block_to_block_type(block),
            "paragraph"
        )

    def test_block_type_ordered(self):
        block = "1. This is an ordered list block\n2. Es\n3. Last"
        self.assertEqual(
            block_to_block_type(block),
            "ordered_list"
        )
    def test_block_type_ordered_fail(self):
        block = "1. This is an ordered list block\n2. Es\nLast"
        self.assertEqual(
            block_to_block_type(block),
            "paragraph"
        )

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = """

###### Some random info yo

1. This is an ordered list block
2. Es
3. Last


* This is an unordered list block
* Second
* 3rd item!

>This is a quote block
>More    
>last bit. 

```def print('Hello world') ```

Some random info yo


"""
