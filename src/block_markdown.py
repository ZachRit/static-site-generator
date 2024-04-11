import re
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def strip_blocks(text):
    return text.lstrip("\n").strip()

def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    return list(filter(None, [strip_blocks(block) for block in blocks]))

def is_quote(text):
    quotes = text.split("\n")
    for quote in quotes:
        if not re.search("^>", quote):
            return False
    return True

def is_unordered_list(text):
    items = text.split("\n")
    for item in items:
        if not re.search("^[*-]", item):
            return False
    return True

def is_ordered_list(text):
    items = text.split("\n")
    if items[0][0] != "1":
        return False
    count = 1
    for item in items:
        if not(re.search("^\d+\.", item) and int(item[0]) == count):
            return False
        count += 1
    return True

def block_to_block_type(block):
    if re.search("^#{1,6}\s.*", block):
        return block_type_heading
    if re.search("^```(?:.|[\r\n])*?```", block):
        return block_type_code
    if is_quote(block):
        return block_type_quote
    if is_unordered_list(block):
        return block_type_unordered_list
    if is_ordered_list(block):
        return block_type_ordered_list
    return block_type_paragraph

def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type ==  block_type_heading:
            nodes.append(heading_to_html(block))
        if block_type == block_type_code:
            nodes.append(code_to_html(block))
        if block_type == block_type_quote:
            nodes.append(quote_to_html(block))
        if block_type == block_type_unordered_list:
            nodes.append(unordered_list_to_html(block))
        if block_type == block_type_ordered_list:
            nodes.append(ordered_list_to_html(block))
        if block_type == block_type_paragraph:
            nodes.append(paragraph_to_html(block))
    return ParentNode("div", nodes)

def text_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def quote_to_html(markdown):
    lines = []
    quotes = markdown.split("\n")
    for quote in quotes:
        if not quote.startswith(">"):
            raise ValueError("Invalid quote block")
        lines.append(quote.lstrip(">").strip())
    quote_lines = " ".join(lines)
    children = text_children(quote_lines)
    return ParentNode("blockquote", children)

def code_to_html(markdown):
    if not markdown.startswith("```") or not markdown.endswith("```"):
        raise ValueError("Invalid code block")
    code_text = markdown.lstrip("`").rstrip("`")
    children = text_children(code_text)
    return ParentNode("pre", [ParentNode("code", children)])

def unordered_list_to_html(markdown):
    nodes = []
    items = markdown.split("\n")
    for item in items:
        item_trimmed = item.lstrip("*").lstrip("-").strip()
        children = text_children(item_trimmed)
        nodes.append(ParentNode("li", children))
    return ParentNode("ul", nodes)

def ordered_list_to_html(markdown):
    nodes = []
    items = markdown.split("\n")
    for item in items:
        item_trimmed = re.sub("^\d+\.", "", item).strip()
        children = text_children(item_trimmed)
        nodes.append(ParentNode("li", children))
    return ParentNode("ol", nodes)

def heading_to_html(markdown):
    heading_text = markdown.lstrip("#").strip()
    heading_type = len(markdown) - len(heading_text) - 1
    if heading_type >= len(markdown):
        raise ValueError("Invalid heading block")
    children = text_children(heading_text)
    return ParentNode(f"h{heading_type}", children)

def paragraph_to_html(markdown):
    lines = markdown.split("\n")
    paragraph = " ".join(lines)
    children = text_children(paragraph)
    return ParentNode("p", children)
