from textnode import TextType, TextNode


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
