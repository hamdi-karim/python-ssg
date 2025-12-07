import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", props={"class": "container"})
        self.assertEqual(node.to_html(), "<p class=container>Hello, world!</p>")

    def test_leaf_to_html_raises_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_none_tag_ignores_props(self):
        node = LeafNode(None, "Click me", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), "Click me")
