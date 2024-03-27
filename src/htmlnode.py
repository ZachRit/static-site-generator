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
    
    def to_html(self):
        if self.tag == None:
            return self.value
        else:
            open_tag = f"<{self.tag}{self.props_to_html()}>" 
            close_tag = f"</{self.tag}>"
            return f"{open_tag}{self.value}{close_tag}"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError
        else:
            super().__init__(tag, value, props=props)

test_node = LeafNode("p", "This is a paragraph of text.", {"class": "test", "href": "hello"}) #the props are not rendering
test_node2 = HTMLNode("p", "This is a paragraph of text.", {"class": "test", "href": "hello"}) #the props are not rendering
print(test_node.to_html())
print(test_node2.to_html())
