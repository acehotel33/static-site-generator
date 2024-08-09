import unittest

from blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(actual, expected)

    def test_markdown_to_blocks_empty_lines(self):
        markdown = "# This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(actual, expected)


class TestBlockToBlockType(unittest.TestCase):
    def test_btbt_h1(self):
        block = '# Heading 1'
        expected = 'h1' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h2(self):
        block = '## Heading 2'
        expected = 'h2' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h3(self):
        block = '### Heading 3'
        expected = 'h3' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h4(self):
        block = '#### Heading 4'
        expected = 'h4' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h5(self):
        block = '##### Heading 5'
        expected = 'h5' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
    
    def test_btbt_h6(self):
        block = '###### Heading 6'
        expected = 'h6' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h6_space(self):
        block = ' ###### Heading 6'
        expected = 'normal paragraph' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h_empty_nospace(self):
        block = '###'
        expected = 'normal paragraph' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_h_empty_withspace(self):
        block = '###### '
        expected = 'h6' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_code(self):
        block = '```some code```'
        expected = 'code' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_code_empty(self):
        block = '``````'
        expected = 'code' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_code_unfinished(self):
        block = '`````'
        expected = 'normal paragraph' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_code_space_end(self):
        block = '`````` '
        expected = 'normal paragraph' 
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_quote(self):
        block = "> Quote line 1\n> Quote line 2\n> Quote line3"
        expected = 'quote'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_quote_no_space(self):
        block = "> Quote line 1\n>Quote line 2\n> Quote line3"
        expected = 'quote'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_quote_missing_start(self):
        block = " Quote line 1\n> Quote line 2\n> Quote line3"
        expected = 'normal paragraph'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_quote_empty(self):
        block = ">\n>\n>"
        expected = 'quote'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_unordered(self):
        block = "- Unordered line 1\n- Unordered line 2\n- Unordered line 3"
        expected = 'unordered list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_unordered_no_space(self):
        block = "- Unordered line 1\n-Unordered line 2\n- Unordered line 3"
        expected = 'normal paragraph'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_unordered_stars(self):
        block = "* Unordered line 1\n* Unordered line 2\n* Unordered line 3"
        expected = 'unordered list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_unordered_mixed(self):
        block = "* Unordered line 1\n- Unordered line 2\n* Unordered line 3"
        expected = 'unordered list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_ordered(self):
        block = "1. Ordered line 1\n2. Ordered line 2\n3. Ordered line 3"
        expected = 'ordered list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_ordered_no_space(self):
        block = "1.Ordered line 1\n2. Ordered line 2\n3. Ordered line 3"
        expected = 'normal paragraph'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_ordered_strange(self):
        block = "1. 2. 3. \n2. \n3. "
        expected = 'ordered list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_btbt_normal_paragraph(self):
        block = "hello mate"
        expected = "normal paragraph"
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()