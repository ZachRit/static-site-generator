import re

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

md = "```\ncode\n```"
print(block_to_block_type(md))
