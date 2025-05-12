import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This isn't a text node", TextType.italic)
        node2 = TextNode("This is a text node", TextType.italic)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.italic)
        node2 = TextNode("This is a text node", TextType.italic, "https://boot.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
