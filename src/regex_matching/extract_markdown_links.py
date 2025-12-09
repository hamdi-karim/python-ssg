"""Utilities for extracting markdown link references from text."""

import re


def extract_markdown_links(text):
    """Return (anchor, url) tuples for markdown links: [text](url)."""

    # Negative lookbehind avoids matching image syntax `![alt](url)`
    pattern = r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)"
    return re.findall(pattern, text)
