# python-ssg

## Text Parsing Helper

`text_to_textnodes` (src/text_to_textnodes.py) converts markdown-like text into a sequence of `TextNode` objects covering plain text, bold (`**`), italic (`_`), code (`` ` ``), links, and images. Example:

```bash
python3 - <<'PY'
from text_to_textnodes import text_to_textnodes
from textnode import TextType

text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

nodes = text_to_textnodes(text)
for node in nodes:
    print(node)
PY
```

Expected output (order preserved):
```
TextNode(This is , text, None)
TextNode(text, bold, None)
TextNode( with an , text, None)
TextNode(italic, italic, None)
TextNode( word and a , text, None)
TextNode(code block, code, None)
TextNode( and an , text, None)
TextNode(obi wan image, image, https://i.imgur.com/fJRm4Vk.jpeg)
TextNode( and a , text, None)
TextNode(link, link, https://boot.dev)
```

## Markdown Block Splitter

`markdown_to_blocks` (`src/markdown_to_blocks.py`) slices a raw Markdown document into logical blocks separated by blank lines (paragraphs, lists, code fences, etc.). It performs a simple `split("\n\n")`, trims leading/trailing whitespace on each block, and skips blank results so downstream parsers can operate on clean chunks.

```bash
python3 - <<'PY'
from markdown_to_blocks import markdown_to_blocks

doc = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

print(markdown_to_blocks(doc))
PY
```

Output:
```
[
  'This is **bolded** paragraph',
  'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
  '- This is a list\n- with items'
]
```
