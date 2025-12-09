from textnode import TextType, TextNode
from extraction_utilities.extract_markdown_images import extract_markdown_images
from extraction_utilities.extract_markdown_links import extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            delimiters_count = old_node.text.count(delimiter)

            if delimiters_count == 0:
                new_nodes.append(old_node)
                continue

            if not delimiters_count % 2 == 0:
                raise ValueError("Invalid Markdown syntax")

            split_pieces = old_node.text.split(delimiter)
            for index in range(len(split_pieces)):
                piece = split_pieces[index]
                if piece == "":
                    continue

                if index % 2 == 0:
                    new_nodes.append(TextNode(piece, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(piece, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    """Split text nodes into text and image nodes using markdown image syntax."""

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(old_node)
            continue

        current = text
        for alt_text, url in matches:
            marker = f"![{alt_text}]({url})"
            parts = current.split(marker, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            current = parts[1]

        if current:
            new_nodes.append(TextNode(current, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    """Split text nodes into text and link nodes using markdown link syntax."""

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(old_node)
            continue

        current = text
        for anchor_text, url in matches:
            marker = f"[{anchor_text}]({url})"
            parts = current.split(marker, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            current = parts[1]

        if current:
            new_nodes.append(TextNode(current, TextType.TEXT))

    return new_nodes
