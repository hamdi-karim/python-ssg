import textwrap


def markdown_to_blocks(markdown):
    """Split a raw markdown document into top-level blocks separated by blank lines."""
    if markdown is None:
        return []

    normalized = textwrap.dedent(markdown)
    if not normalized.strip():
        return []

    blocks = []
    current_lines = []

    for line in normalized.strip("\n").split("\n"):
        if line.strip() == "":
            if current_lines:
                blocks.append("\n".join(current_lines).strip("\n"))
                current_lines = []
            continue
        current_lines.append(line)

    if current_lines:
        blocks.append("\n".join(current_lines).strip("\n"))

    return blocks
