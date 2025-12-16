"""Utilities for extracting the document title from markdown text."""


def extract_title(markdown):
    """
    Return the first h1 heading from the markdown string.

    The title is derived from a line starting with a single ``#`` followed by
    text. Leading/trailing whitespace around the title is stripped. Raises a
    ValueError if no h1 is present.
    """

    for line in markdown.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith("# "):
            return stripped_line[1:].strip()
    raise ValueError("No h1 header found in markdown")
