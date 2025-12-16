import os
import shutil

from extraction_utilities.extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def copy_files_recursive(source_dir_path, dest_dir_path):
    """
    Recursively copy the contents of source_dir into destination_dir.
    The destination directory is cleared before copying to ensure a clean state.
    """
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    """
    Render a markdown file into a full HTML page using the provided template.

    The template should include {{ Title }} and {{ Content }} placeholders.
    """

    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )

    with open(from_path, "r") as markdown_file:
        markdown = markdown_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page_html = (
        template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as output_file:
        output_file.write(page_html)


def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    """Generate HTML pages for all markdown files under content_dir_path."""

    for root, _, files in os.walk(content_dir_path):
        for filename in files:
            if not filename.endswith(".md"):
                continue

            from_path = os.path.join(root, filename)
            relative_path = os.path.relpath(from_path, content_dir_path)
            dest_path = os.path.join(
                dest_dir_path, relative_path.replace(".md", ".html")
            )
            generate_page(from_path, template_path, dest_path)


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating site pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


if __name__ == "__main__":
    main()
