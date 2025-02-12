from textnode import TextNode, TextType

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
