import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_detects_hash_prefix(self):
        block = "### Heading Three"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_invalid_heading_without_space_is_paragraph(self):
        block = "##NoSpace Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> quote line\n> continued"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- first item\n- second item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_invalid_sequence_is_paragraph(self):
        block = "1. first\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_fallback(self):
        block = "This is a normal paragraph block."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_none_block_raises(self):
        with self.assertRaises(ValueError):
            block_to_block_type(None)

    def test_empty_block_raises(self):
        with self.assertRaises(ValueError):
            block_to_block_type("")
