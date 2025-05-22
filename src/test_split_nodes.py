import unittest
from textnode import TextNode, TextType
from split_nodes import *

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_split_with_delimiter(self):
        # Test a basic case with code delimiters
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.text)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.code)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.text)
    
    def test_no_delimiter(self):
        # Test with no delimiters
        node = TextNode("This is plain text", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.text)

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block`"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 6
        assert nodes[0].text == "This is "
        assert nodes[1].text == "text"
        assert nodes[1].text_type == TextType.bold
        # Add more assertions to test the rest of the nodes

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
