import os
import shutil
import sys

from copy_static import copy_files_recursive
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = "/" if len(sys.argv) < 2 else sys.argv[1]
    if not basepath.endswith("/"):
        basepath += "/"

    print(f"Using base path: {basepath}")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath,
    )


if __name__ == "__main__":
    main()
