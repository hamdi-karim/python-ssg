"""Utilities for extracting markdown image references from text."""

import re


def extract_markdown_images(text):
    """Return a list of (alt, url) tuples for markdown images: ![alt](url)."""

    pattern = r"!\[([^\]]*)\]\(([^)\s]+)\)"
    return re.findall(pattern, text)
