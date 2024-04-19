import os, shutil
from copystatic import copy_directory
from generate_page import generate_page_recursive

def main():
    del_public_directory()
    copy_directory("./static", "./public")
    print("Copied files to public directory...")
    generate_page_recursive("./content", "./template.html", "./public")

def del_public_directory():
    if os.path.exists("./public"):
        shutil.rmtree("./public")

main()
