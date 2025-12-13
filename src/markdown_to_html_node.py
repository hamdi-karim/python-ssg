from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


# converts a full markdown document into HTMLNode
# (which contains multiple HTMLNodes children)
def markdown_to_html_node(markdown):

    # Split the markdown into blocks (you already have a function for this)
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        if not block:
            continue
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children.append(_paragraph_node(block))
            case BlockType.HEADING:
                children.append(_heading_node(block))
            case BlockType.CODE:
                children.append(_code_node(block))
            case BlockType.QUOTE:
                children.append(_quote_node(block))
            case BlockType.UNORDERED_LIST:
                children.append(_unordered_list_node(block))
            case BlockType.ORDERED_LIST:
                children.append(_ordered_list_node(block))
            case _:
                raise ValueError(f"Unhandled block type: {block_type}")

    return ParentNode("div", children)


def _paragraph_node(block):
    text = " ".join(block.split("\n"))
    return ParentNode("p", _text_to_children(text))


def _heading_node(block):
    hashes, text = block.split(" ", 1)
    level = len(hashes)
    return ParentNode(f"h{level}", _text_to_children(text))


def _code_node(block):
    """Return a pre/code node without inline markdown parsing."""
    lines = block.split("\n")
    code_text = "\n".join(lines[1:-1]) + "\n"
    code_child = text_node_to_html_node(TextNode(code_text, TextType.CODE))
    return ParentNode("pre", [code_child])


def _quote_node(block):
    stripped = [line.lstrip(">").strip() for line in block.split("\n")]
    text = " ".join(stripped)
    return ParentNode("blockquote", _text_to_children(text))


def _unordered_list_node(block):
    items = []
    for line in block.split("\n"):
        content = line.lstrip("- ").strip()
        items.append(ParentNode("li", _text_to_children(content)))
    return ParentNode("ul", items)


def _ordered_list_node(block):
    items = []
    for line in block.split("\n"):
        _, content = line.split(". ", 1)
        items.append(ParentNode("li", _text_to_children(content.strip())))
    return ParentNode("ol", items)


def _text_to_children(text):
    """Convert inline markdown text into HTMLNodes."""
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]
