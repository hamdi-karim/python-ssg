import os
import tempfile
import unittest

from main import generate_page, generate_pages_recursive


class TestGeneratePage(unittest.TestCase):
    def test_generates_full_page_and_creates_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            markdown_path = os.path.join(tmpdir, "page.md")
            template_path = os.path.join(tmpdir, "template.html")
            dest_path = os.path.join(tmpdir, "nested", "index.html")

            with open(markdown_path, "w") as markdown_file:
                markdown_file.write("# Hello\n\nParagraph text")

            with open(template_path, "w") as template_file:
                template_file.write(
                    "<html><head><title>{{ Title }}</title></head>"
                    "<body>{{ Content }}</body></html>"
                )

            generate_page(markdown_path, template_path, dest_path)

            with open(dest_path, "r") as output_file:
                output = output_file.read()

            self.assertIn("<title>Hello</title>", output)
            self.assertIn("<div><h1>Hello</h1><p>Paragraph text</p></div>", output)

    def test_raises_when_no_h1(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            markdown_path = os.path.join(tmpdir, "page.md")
            template_path = os.path.join(tmpdir, "template.html")
            dest_path = os.path.join(tmpdir, "index.html")

            with open(markdown_path, "w") as markdown_file:
                markdown_file.write("No heading here")

            with open(template_path, "w") as template_file:
                template_file.write("{{ Title }} {{ Content }}")

            with self.assertRaises(ValueError):
                generate_page(markdown_path, template_path, dest_path)

    def test_base_path_replaces_root_links(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            markdown_path = os.path.join(tmpdir, "page.md")
            template_path = os.path.join(tmpdir, "template.html")
            dest_path = os.path.join(tmpdir, "index.html")

            with open(markdown_path, "w") as markdown_file:
                markdown_file.write("# Hello\n\nContent")

            with open(template_path, "w") as template_file:
                template_file.write(
                    '<a href="/home">Home</a><img src="/img.png" />{{ Content }}'
                )

            generate_page(markdown_path, template_path, dest_path, base_path="/blog")

            with open(dest_path, "r") as output_file:
                output = output_file.read()

            self.assertIn('href="/bloghome"', output)
            self.assertIn('src="/blogimg.png"', output)

    def test_generate_pages_recursive_builds_nested_structure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            content_root = os.path.join(tmpdir, "content")
            os.makedirs(os.path.join(content_root, "blog", "post"), exist_ok=True)

            index_md = os.path.join(content_root, "index.md")
            blog_md = os.path.join(content_root, "blog", "post", "index.md")
            template_path = os.path.join(tmpdir, "template.html")
            dest_root = os.path.join(tmpdir, "public")

            with open(index_md, "w") as index_file:
                index_file.write("# Home\n\nWelcome")

            with open(blog_md, "w") as blog_file:
                blog_file.write("# Blog Post\n\nContent")

            with open(template_path, "w") as template_file:
                template_file.write(
                    "<html><head><title>{{ Title }}</title></head>"
                    "<body>{{ Content }}</body></html>"
                )

            generate_pages_recursive(content_root, template_path, dest_root, base_path="/blog")

            with open(os.path.join(dest_root, "index.html")) as index_output:
                self.assertIn("<title>Home</title>", index_output.read())

            with open(os.path.join(dest_root, "blog", "post", "index.html")) as post:
                contents = post.read()
                self.assertIn("<title>Blog Post</title>", contents)
                self.assertIn("<h1>Blog Post</h1>", contents)


if __name__ == "__main__":
    unittest.main()
