import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return(matches)

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return(matches)

def split_nodes_image(old_nodes):
    result = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.text:
            result.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if not images:
            result.append(old_node)
            continue

        remaining_text = old_node.text

        for alt_text, image_url in images:
            parts = remaining_text.split(f"![{alt_text}]({image_url})", 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.text))

            result.append(TextNode(alt_text, TextType.image, image_url))

            remaining_text = parts[1] if len(parts) > 1 else ""

        if remaining_text:
            result.append(TextNode(remaining_text, TextType.text))

    return result

def split_nodes_link(old_nodes):
    result = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.text:
            result.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            result.append(old_node)
            continue

        remaining_text = old_node.text

        for link_text, link_url in links:
            parts = remaining_text.split(f"[{link_text}]({link_url})", 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.text))

            result.append(TextNode(link_text, TextType.link, link_url))

            remaining_text = parts[1] if len(parts) > 1 else ""

        if remaining_text:
            result.append(TextNode(remaining_text, TextType.text))

    return result
