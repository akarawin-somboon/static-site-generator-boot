from textnode import TextNode, TextType
from extract_link import split_nodes_image, split_nodes_link
from htmlnode import text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type == TextType.text:
            text = old_node.text

            if delimiter in text:
                start_index = text.find(delimiter)
                end_index = text.find(delimiter, start_index + len(delimiter))

                if end_index == -1:
                    raise Exception(f"No closing delimiter '{delimiter}' found")

                # 1. Text before the delimiter
                before_text = text[:start_index]

                # 2. Text between delimiter (without the delimiters)
                between_text = text[start_index + len(delimiter):end_index]

                #3. Text after the delimeter
                after_text = text[end_index + len(delimiter):]

                if before_text:
                    new_nodes.append(TextNode(before_text, TextType.text))

                new_nodes.append(TextNode(between_text, text_type))

                if after_text:
                    new_nodes.append(TextNode(after_text, TextType.text))
            else:
                new_nodes.append(old_node)

        else:
            new_nodes.append(old_node)
    return new_nodes

def text_to_textnodes(text):
    # Start with a list containing a single TextNode with all the text
    nodes = [TextNode(text, TextType.text)]
    
    # Apply each splitting function in sequence
    # For delimiters (bold, italic, code)
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "_", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    
    # For images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []

    for block in blocks:
        cleaned_block = block.strip()
        if cleaned_block:
            cleaned_blocks.append(cleaned_block)
        
    return cleaned_blocks

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]
