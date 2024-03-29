from textnode import TextNode
from textnode import text_type_text, text_type_bold, text_type_italic, text_type_code

#this function will only support a single level of nesting (one delimiter type)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old_nodes is an array of nodes (LeafNodes, ParentNodes, HTMLNodes)
    nodes = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            nodes.append(old_node)
        else:
            split_nodes = old_node.text.split(delimiter)
            if len(split_nodes) % 2 == 1:
                for i in range(len(split_nodes)):
                    if i % 2 == 0 and not split_nodes[i] == '':
                        nodes.append(TextNode(split_nodes[i], text_type_text))
                    if i % 2 == 1:
                        nodes.append(TextNode(split_nodes[i], text_type))
            else:
                raise ValueError("Invalid markdown. Missing closing delimiter")
    return nodes
