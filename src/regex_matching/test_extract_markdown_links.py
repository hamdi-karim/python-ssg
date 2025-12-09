import unittest

from regex_matching.extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and "
            "[to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_multiple_links(self):
        matches = extract_markdown_links("[one](https://one.com)[two](https://two.com)")
        self.assertListEqual(
            [("one", "https://one.com"), ("two", "https://two.com")], matches
        )

    def test_ignores_images(self):
        matches = extract_markdown_links(
            "![alt](https://img.com/pic.png) and [link](https://site.com)"
        )
        self.assertListEqual([("link", "https://site.com")], matches)

    def test_no_links_returns_empty(self):
        matches = extract_markdown_links("Plain text without any markdown links.")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
