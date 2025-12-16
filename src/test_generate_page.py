import os
import tempfile
import unittest

from main import generate_page


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


if __name__ == "__main__":
    unittest.main()
