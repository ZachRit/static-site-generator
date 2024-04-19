from block_markdown import markdown_to_blocks, markdown_to_html_node
import re, os

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        heading = re.findall("^#\s.+", block)
        if heading:
            return block.lstrip("# ").strip()
    raise Exception("File must contain at least one h1")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = open(from_path, "r").read()
    template = open(template_path, "r").read()
    html = markdown_to_html_node(md).to_html()
    if not os.path.dirname(dest_path):
        os.makedirs(dest_path)
    output_html = template.replace("{{ Title }}", extract_title(md), 1).replace("{{ Content }}", html, 1)
    with open(os.path.join(dest_path, "index.html"), "w") as file:
        file.write(output_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        print(file)
        content_path = os.path.join(dir_path_content, file)
        content_dest_path = os.path.join(dest_dir_path, file)
        if os.path.isdir(content_path):
            os.makedirs(content_dest_path)
            generate_page_recursive(content_path, template_path, content_dest_path)
        else:
            generate_page(content_path, template_path, dest_dir_path)
