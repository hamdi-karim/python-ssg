from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
    """Return the BlockType for a given markdown block."""
    if markdown_block is None:
        raise ValueError("markdown_block cannot be None")

    block = markdown_block
    if block == "":
        raise ValueError("markdown_block cannot be empty")

    lines = block.split("\n")

    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if _is_ordered_list(lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def _is_ordered_list(lines):
    for index, line in enumerate(lines, start=1):
        expected_prefix = f"{index}. "
        if not line.startswith(expected_prefix):
            return False
    return True
