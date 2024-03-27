from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
       
def text_node_to_html_node(text_node):
    if text_node.text_type is not "text" or "bold" or "italic" or "code" or "link" or "image":
        raise Exception("Unsupported text type")
    if text_node.text_type == "text":
        return LeafNode(None, text_node.value)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.value)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.value)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.value)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.value, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.value})

