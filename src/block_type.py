from enum import Enum


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block):
    if block and block[0] == '#':
        i = 0
        while i < len(block) and i < 6 and block[i] == '#':
            i += 1
        # Check if # is followed by a space
        if i < len(block) and block[i] == ' ':
            return BlockType.heading

        # Check if it's a code block
    if len(block) >= 6 and block[:3] == "```" and block[-3:] == "```":
        return BlockType.code

    if len(block) > 0:
        lines = block.split('\n')
        if all(line.startswith('>') for line in lines):
            return BlockType.quote

        if all(line.startswith('- ') for line in lines):
            return BlockType.unordered_list

        is_ordered = True
        for i, line in enumerate(lines):
            expected_prefix = f"{i+1}. "
            if not line.startswith(expected_prefix):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ordered_list

    return BlockType.paragraph
