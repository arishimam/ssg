class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and 
            self.children == other.children and
            self.props == other.props
        )

    def __to_html__(self):
        raise NotImplementedError("to_html method not implemented")

    def __props_to_html__(self):
        if self.props == None:
            return ""

        prop_string = ""
        for k,v in self.props.items():
            prop_string += f" {k}=\"{v}\"" 
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __to_html__(self):
        if self.value == None:
            raise ValueError("Invalid html, no value!")

        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.__props_to_html__()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

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

    def __repr__(self):
        return f"ParentNode({self.tag}, children:{self.children}, {self.props})"

