from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __to_html__(self):
        if self.tag == None:
            raise ValueError("Tag is missing!")

        if self.children == None:
            raise ValueError("Children missing!")

        html_string = f"<{self.tag}{self.__props_to_html__()}>"
        for c in self.children:
            html_string += c.__to_html__()

        
        html_string += f"</{self.tag}>"

        return html_string
