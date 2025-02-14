import re
from textnode import * 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []

    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            nodes.append(n)
            continue

        if n.text.count(delimiter)%2 != 0:
            raise Exception("Invalid markdown syntax!")

        d_closed = True
        i = 0
        prev_i = 0
        j = 0
        new_nodes = []

        while i < len(n.text):
            if n.text[i] == delimiter[0]:
                j = i
                while n.text[j] == delimiter[j-i]:
                    if j - i + 1 == len(delimiter):
                        if d_closed == False:
                            new_nodes.append(TextNode(n.text[prev_i:j-len(delimiter)+1], text_type))
                        else:
                            new_nodes.append(TextNode(n.text[prev_i:j-len(delimiter)+1], n.text_type))

                        i = j+1 
                        prev_i = i 
                        d_closed = not d_closed
                    j+=1

            i+=1

            if i == len(n.text):
                new_nodes.append(TextNode(n.text[prev_i:], n.text_type))

        nodes.extend(new_nodes)

    return nodes

def extract_markdown_images(text):
    image_links = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_links

def extract_markdown_links(text):
    text_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text) 
    return text_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for o in old_nodes:
        if o.text_type != TextType.TEXT:
            new_nodes.append(o)
            continue

        original_text = o.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(o)
            continue

        for img in images:
            sections = original_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed!")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))

            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for o in old_nodes:
        if o.text_type != TextType.TEXT:
            new_nodes.append(o)
            continue

        original_text = o.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(o)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed!")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


    
def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)

    nodes = split_nodes_image([text_node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes


