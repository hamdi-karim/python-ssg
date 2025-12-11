import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_input_returns_empty_list(self):
        self.assertEqual(markdown_to_blocks("   \n \n"), [])

    def test_multiple_blank_lines_do_not_add_empty_blocks(self):
        md = "First paragraph\n\n\n\nSecond paragraph\n\n\nThird"
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "First paragraph",
                "Second paragraph",
                "Third",
            ],
        )

    def test_block_stripping_preserves_internal_lines(self):
        md = """- item one
  - nested bullet
  - nested bullet 2

    code fence start
    line two"""
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "- item one\n  - nested bullet\n  - nested bullet 2",
                "code fence start\n    line two",
            ],
        )
