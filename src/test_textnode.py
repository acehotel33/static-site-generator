import unittest

from textnode import TextNode, split_nodes_delimiter

text_type_text="text"
text_type_code="code"
text_type_bold="bold"
text_type_italic="italic"


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is not a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", 'hi.com')
        node2 = TextNode("This is a text node", "bold", 'hi.com')
        self.assertEqual(node, node2)


    def test_uneq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "yo")
        self.assertNotEqual(node, node2)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("`code block` at the start and `at the end`", text_type_text)        
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [TextNode("code block", "code", None), TextNode(" at the start and ", "text", None), TextNode("at the end", "code", None)]
        actual = new_nodes
        self.assertEqual(expected, actual)

    def test_code_split_multiple(self):
        node1 = TextNode("`code block` at the start and `at the end`", text_type_text)        
        node2 = TextNode("Now it's `in the middle` and this is just text", text_type_text)
        node3 = TextNode("This is simply empty text", text_type_text)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "`", text_type_code)
        expected = [
            TextNode("code block", "code", None), 
            TextNode(" at the start and ", "text", None), 
            TextNode("at the end", "code", None),
            TextNode("Now it's ", "text", None),
            TextNode("in the middle", "code", None),
            TextNode(" and this is just text", "text", None),
            TextNode("This is simply empty text", "text", None)
            ]
        actual = new_nodes
        self.assertEqual(expected, actual)

    def test_code_split_only_text(self):
        node = TextNode("Simply text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [TextNode("Simply text", "text", None)]
        actual = new_nodes
        self.assertEqual(expected, actual)

    def test_bold_split(self):
        node = TextNode("**Bold** at the start and **at the end**", text_type_text)        
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [TextNode("Bold", "bold", None), TextNode(" at the start and ", "text", None), TextNode("at the end", "bold", None)]
        actual = new_nodes
        self.assertEqual(expected, actual)  

    def test_invalid_markdown_syntax(self):
        node = TextNode("`code block at the start and  `at the end`", "text")
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", "code")
        self.assertEqual(str(context.exception), "Node has invalid Markdown syntax: missing opening or closing delimiter")

    def test_non_text_nodes(self):
        node = TextNode("This is a non-text node", "code")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        expected = [node]
        self.assertEqual(new_nodes, expected)


# node1 = TextNode("`code block` at the start and `at the end`", text_type_text)
# # new_nodes = split_nodes_delimiter([node], "`", text_type_code)
# # print(new_nodes)
# node2 = TextNode("This is text with a `code block` word", text_type_text)
# # new_nodes2 = split_nodes_delimiter([node2], "`",  text_type_code)

# node3 = TextNode("This is a regular text", text_type_text)
# new_nodes = split_nodes_delimiter([node1, node2, node3], "`", text_type_code)
# print(new_nodes)


if __name__ == "__main__":
    unittest.main()