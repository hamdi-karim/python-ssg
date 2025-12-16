import unittest

from extraction_utilities.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extracts_first_h1(self):
        markdown = "# Hello\n\nSome content\n## Subheading"
        self.assertEqual("Hello", extract_title(markdown))

    def test_strips_whitespace_and_ignores_other_headings(self):
        markdown = "Intro line\n #  Welcome Home   \n### Deep Dive"
        self.assertEqual("Welcome Home", extract_title(markdown))

    def test_raises_when_missing_h1(self):
        markdown = "## No top level\nJust text"
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
