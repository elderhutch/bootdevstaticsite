import os
import shutil
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
   
    def copy_to_public():
        if os.path.isdir("./public"):
            shutil.rmtree("./public/")
        shutil.copytree("./static/", "./public/")
    copy_to_public()
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
'''
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )
'''



main()
