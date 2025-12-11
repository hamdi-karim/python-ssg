def markdown_to_blocks(markdown):
    """Split a markdown document into blocks separated by blank lines."""

    if not markdown:
        return []

    if not markdown.strip():
        return []

    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
