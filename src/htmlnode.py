class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def props_to_html(self):
        prop_list = ""
        if self.props is not None:
            for key, value in self.props.items():
                prop_list += f' {key}="{value}"'
            return prop_list
        else:
            return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == None:
            return self.value
        if self.value == None:
            raise ValueError("Value cannot be blank")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("A tag must be provided")
        if self.children == None:
            raise ValueError("No child elements provided")
        result = ''
        for child in self.children:
            result += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'

