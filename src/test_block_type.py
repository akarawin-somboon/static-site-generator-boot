import unittest
from block_type import block_to_block_type, BlockType

class TestBlockTypeDetection(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.heading)
        self.assertEqual(block_to_block_type("###### Level 6 heading"), BlockType.heading)
        # Test that 7 '#' characters should NOT be a heading
        self.assertNotEqual(block_to_block_type("####### Too many"), BlockType.heading)
        # Test that no space after '#' should NOT be a heading
        self.assertNotEqual(block_to_block_type("#NoSpace"), BlockType.heading)
        
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.code)
        self.assertEqual(block_to_block_type("```\n```"), BlockType.code)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type(">quote"), BlockType.quote)
        self.assertEqual(block_to_block_type(">line 1\n>line 2"), BlockType.quote)
        # Test that missing '>' on any line should be treated as paragraph
        self.assertEqual(block_to_block_type(">line 1\nline 2"), BlockType.paragraph)
        
if __name__ == '__main__':
    unittest.main()
