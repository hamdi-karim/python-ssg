import unittest

from extraction_utilities.extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "![first](https://img.com/1.png) text ![second](https://img.com/2.jpg)"
        )
        self.assertListEqual(
            [
                ("first", "https://img.com/1.png"),
                ("second", "https://img.com/2.jpg"),
            ],
            matches,
        )

    def test_empty_alt_text(self):
        matches = extract_markdown_images("![ ](https://img.com/blank.png)")
        self.assertListEqual([(" ", "https://img.com/blank.png")], matches)

    def test_no_images_returns_empty(self):
        matches = extract_markdown_images("No images here, just text.")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
