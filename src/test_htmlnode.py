import unittest
from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with empty props
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        # Note: order might vary, so we check for both possible orders
        result = node.props_to_html()
        self.assertTrue(
            result == ' href="https://www.google.com" target="_blank"' or 
            result == ' target="_blank" href="https://www.google.com"'
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
