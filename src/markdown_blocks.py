from inline_markdown import text_to_text_node 
from textnode import text_node_to_html_node 
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    # use regular expression to split 2+ new line characters
    blocks = re.split(r"(\n{2,})", markdown)
    filtered_blocks = []

    for b in blocks:
        b = b.strip("\n")
        b = b.strip()

        if b == "":
            continue
        
        filtered_blocks.append(b)

    return filtered_blocks 


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith( ('# ', '## ', '### ', '#### ', '##### ', '###### ') ):
        return block_type_heading

    if block.startswith('```') and block.endswith('```'):
        return block_type_code

    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote

    if block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i+=1

        return block_type_ordered_list

    return block_type_paragraph

def markdown_to_html_node(markdown):
    # split into blocks
    # call block_to_html_node helper function
    # wrap results in parent div then return

    blocks = markdown_to_blocks(markdown)

    nodes = []

    for b in blocks:

        if block_to_block_type(b) == "heading":
            i = 0
            while b[i] == '#':
                i+=1
            b = b.lstrip("#")
            b = b.strip()

            text_node = TextNode(b, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            html_node.tag = f"h{i}"
            nodes.append(html_node)
            continue

        if block_to_block_type(b) == "paragraph":
            # create TextNode
            text_node = TextNode(b, TextType.TEXT)
            para_node = text_node_to_html_node(text_node)
            para_node.tag = "p"
            nodes.append(para_node)
            continue

        if block_to_block_type(b) == "code":
            b = b.strip('```') 
            text_node = TextNode(b.strip(), TextType.CODE)
            code_node = text_node_to_html_node(text_node)
            code_node.tag = "code"
            pre_node = ParentNode("pre", [code_node], None)
            nodes.append(pre_node)
            continue

        if block_to_block_type(b) == "quote":
            lines = b.split('\n') 
            quote_nodes = []
            
            for i in range(len(lines)):
                lines[i] = lines[i].lstrip('>')
                lines[i] = lines[i].strip() 

            quote_block = " ".join(lines)

            text_node = TextNode(quote_block, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)

            quote_block_node = ParentNode("blockquote", html_node, None)
            nodes.append(quote_block_node)
            continue

        if block_to_block_type(b) == "unordered_list":
            if b[0] == '*':
                lines = b.split('*')
            else:
                lines = b.split('-')

            list_nodes = []

            for l in lines:
                if l == "":
                    continue
                l_text_node = TextNode(l.strip(), TextType.TEXT)
                l_html_node = text_node_to_html_node(l_text_node)
                l_html_node.tag = "li"
                list_nodes.append(l_html_node)

            list_block = ParentNode("ul", list_nodes, None)
            nodes.append(list_block)
            continue

        if block_to_block_type(b) == "ordered_list":
            lines = b.split("\n")
            list_nodes = []
            i = 1

            for l in lines:
                l = l.strip(f"{i}. ")
                i+=1
                l_text_node = TextNode(l, TextType.TEXT)
                l_html_node = text_node_to_html_node(l_text_node)
                l_html_node.tag = "li"
                list_nodes.append(l_html_node)

            list_block = ParentNode("ol", list_nodes, None)
            nodes.append(list_block)
            continue

    return ParentNode("div", nodes, None) 



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

Some more random info


"""
print(markdown_to_html_node(md))

    
