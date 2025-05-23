from split_nodes import markdown_to_blocks, text_to_children
from block_type import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from textnode import TextNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.paragraph:
            children = text_to_children(block)
            node = ParentNode("p", children)
            html_nodes.append(node)
        elif block_type == BlockType.heading:
            block = block.split(" ", 1)
            level = len(block[0])
            text = block[1]
            children = text_to_children(text)
            node = ParentNode("h" + str(level), children)
            html_nodes.append(node)
        elif block_type == BlockType.unordered_list:
            items = block.splitlines()
            li_nodes = []
            for item in items:
                item = item[2:]
                children = text_to_children(item)
                list_node = ParentNode("li", children)
                li_nodes.append(list_node)
            html_nodes.append(ParentNode("ul", li_nodes))
        elif block_type == BlockType.ordered_list:
            items = block.splitlines()
            li_nodes = []
            for item in items:
                split_item = item.split(". ", 1)
                if len(split_item) > 1:
                    text = split_item[1]
                    children = text_to_children(text)
                    li_node = ParentNode("li", children)
                    li_nodes.append(li_node)
            node = ParentNode("ol", li_nodes)
            html_nodes.append(node)
        elif block_type == BlockType.code:
            lines = block.splitlines()
            code_content = "\n".join(lines[1:-1])
            code_leaf = LeafNode("code", code_content)
            pre_node = ParentNode("pre", [code_leaf])
            html_nodes.append(pre_node)
        elif block_type == BlockType.quote:
            clean_lines = []
            for line in block.splitlines():
                if line.startswith("> "):
                    clean_lines.append(line[2:])
                elif line.startswith(">"):
                    clean_lines.append(line[1:])
            quote_text = "\n".join(clean_lines)
            children = text_to_children(quote_text)
            node = ParentNode("blockquote", children)
            html_nodes.append(node)

    return ParentNode("div", html_nodes)
