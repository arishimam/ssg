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
        raise NotImplementedError()

    def __props_to_html__(self):
        if self.props == None:
            return ""

        prop_string = ""
        for k,v in self.props.items():
            prop_string += f" {k}=\"{v}\"" 
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

