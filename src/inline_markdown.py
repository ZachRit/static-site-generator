from textnode import TextNode
from textnode import text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
import re

# This function will only support a single level of nesting (one delimiter type)
# I will probably add support for multiple delimiters some other time
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
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

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            nodes.append(old_node)
            continue
        old_text_copy = old_node.text
        extracted_images = extract_markdown_images(old_text_copy)
        if extracted_images == []:
            nodes.append(old_node)
        else:
            for extracted_image in extracted_images:
                split_image = old_text_copy.split(f"![{extracted_image[0]}]({extracted_image[1]})", 1)
                if len(split_image) != 2:
                    raise ValueError("Invalid markdown. Image tag improperly formatted")
                if split_image[0] == "":
                    nodes.append(TextNode(extracted_image[0], text_type_image, extracted_image[1]))
                else:
                    nodes.append(TextNode(split_image[0], text_type_text))
                    nodes.append(TextNode(extracted_image[0], text_type_image, extracted_image[1]))
                old_text_copy = split_image[1] 
            if old_text_copy != "":
                nodes.append(TextNode(old_text_copy, text_type_text))
    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            nodes.append(old_node)
            continue
        old_text_copy = old_node.text
        extracted_links = extract_markdown_links(old_text_copy)
        if extract_markdown_links == []:
            nodes.append(old_node)
        else:
            for extracted_link in extracted_links:
                split_link = old_text_copy.split(f"[{extracted_link[0]}]({extracted_link[1]})", 1)
                if len(split_link) != 2:
                    raise ValueError("Invalid markdown. Link tag improperly formatted")
                if split_link == "":
                    nodes.append(TextNode(extracted_link[0], text_type_link, extracted_link[1]))
                else:
                    nodes.append(TextNode(split_link[0], text_type_text))
                    nodes.append(TextNode(extracted_link[0], text_type_link, extracted_link[1]))
                old_text_copy = split_link[1]
            if old_text_copy != "":
                nodes.append(TextNode(old_text_copy, text_type_text))
    return nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, '**', text_type_bold)
    nodes = split_nodes_delimiter(nodes, '*', text_type_italic)
    nodes = split_nodes_delimiter(nodes, '`', text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
