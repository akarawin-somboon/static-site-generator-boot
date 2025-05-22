from split_nodes import markdown_to_blocks, text_to_children
from block_type import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode


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

