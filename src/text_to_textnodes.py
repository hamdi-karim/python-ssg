"""Convert markdown-like text into structured TextNode instances."""

from textnode import TextNode, TextType
from split_nodes_delimiter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


def text_to_textnodes(text: str) -> list[TextNode]:
    """Parse text into TextNodes for bold, italic, code, links, and images."""

    nodes = [TextNode(text, TextType.TEXT)]

    # Preserve link/image URLs by splitting them before delimiter parsing.
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
