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

tester = LeafNode("p", "this is a hello world test", {"class": "hello", "id": "world"})
print(tester.to_html())

tester2 = LeafNode("p", "this is a hello world test")
print(tester2.to_html())

tester3 = LeafNode(None, "this is a hello world test")
print(tester3.to_html())
