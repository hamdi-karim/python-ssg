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
