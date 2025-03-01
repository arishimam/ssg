from inline_markdown import text_to_text_nodes 
from textnode import text_node_to_html_node 
from htmlnode import ParentNode, LeafNode
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
    blocks = markdown_to_blocks(markdown)
    nodes = []

    # call block_to_html_node helper function
    for b in blocks:
        html_node = block_to_html_node(b)
        nodes.append(html_node)

    # wrap results in parent div then return
    return ParentNode("div", nodes, None) 

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html(block)
    if block_type == block_type_heading:
        return heading_to_html(block)
    if block_type == block_type_code:
        return code_to_html(block)
    if block_type == block_type_quote:
        return quote_to_html(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_html(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html(block)
    ValueError("Invalid block type!")

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children 

def paragraph_to_html(b):
    lines = b.split("\n")
    paragraph = " ".join(lines) 
    children = text_to_children(b)
    return ParentNode("p", children, None)
    

def heading_to_html(b):
    i = 0
    while b[i] == '#':
        i+=1
    b = b.lstrip("#")
    b = b.strip()

    children = text_to_children(b)

    return ParentNode(f"h{i}", children, None)


def code_to_html(b):
    text = b[3:-3]
    children = text_to_children(text)
    code = ParentNode("code", children, None)
    return ParentNode("pre", [code], None)


def quote_to_html(b):

    lines = b.split('\n') 
    new_lines = [] 
    for i in range(len(lines)):
        
        lines[i] = lines[i].lstrip('> ')
        lines[i] = lines[i].strip() 
        #   if lines[i] == "":
            #continue
        new_lines.append(lines[i])

    quote_block = " ".join(new_lines)
    children = text_to_children(quote_block)
    return ParentNode("blockquote", children, None)

def unordered_list_to_html(b):

    lines = b.split('\n')

    list_nodes = []

    for l in lines:
        if l == "":
            continue
        l = l[2:]
        line_children = text_to_children(l.strip())
        line = ParentNode("li", line_children, None)
        list_nodes.append(line)

    return ParentNode("ul", list_nodes, None)


def ordered_list_to_html(b):
    lines = b.split("\n")
    list_nodes = []

    i = 1
    for l in lines:
        l = l.lstrip(f"{i}. ")
        i+=1
        line_children = text_to_children(l)
        line = ParentNode("li", line_children, None)
        list_nodes.append(line)

    return ParentNode("ol", list_nodes, None)


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

#doc = markdown_to_html_node(md)
#print(doc.__to_html__())

    
