from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def __to_html__(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.__props_to_html__()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
