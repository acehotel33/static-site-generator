import unittest

from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

text_type_text="text"
text_type_code="code"
text_type_bold="bold"
text_type_italic="italic"
text_type_image="image"
text_type_link="link"


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
        expected = [
            TextNode("code block", "code", None), 
            TextNode(" at the start and ", "text", None), 
            TextNode("at the end", "code", None)]
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

    def test_code_split_embedded_bold(self):
        node = TextNode("This is some **bold** text that also contains a `piece of code` within it", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
            TextNode("This is some **bold** text that also contains a ", "text", None),
            TextNode("piece of code", "code", None),
            TextNode(" within it", "text", None)
            ]
        actual = new_nodes
        self.assertEqual(expected, actual)

    def test_bold_split_embedded_code(self):
        node = TextNode("This is some **bold** text that also contains a `piece of code` within it", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is some ", "text", None),
            TextNode("bold", "bold", None),
            TextNode(" text that also contains a `piece of code` within it", "text", None)
            ]
        actual = new_nodes
        self.assertEqual(expected, actual)


class TestSplitNodesImage(unittest.TestCase):
    def test_split_node_image(self):
        node = TextNode(
        "These are images ![alt text](https://www.boot.dev) and ![alt text 2](https://www.youtube.com/@bootdotdev)", text_type_text)
        expected = [
            TextNode("These are images ", "text"), 
            TextNode("alt text", "image", "https://www.boot.dev"), 
            TextNode(" and ", "text"), 
            TextNode("alt text 2", "image", "https://www.youtube.com/@bootdotdev")]
        actual = split_nodes_image([node])
        self.assertEqual(actual, expected)

    def test_split_node_image_embedded_code(self):
        node = TextNode(
        "These are images ![alt text](https://www.boot.dev) and ![alt text 2](https://www.youtube.com/@bootdotdev) but surprise! we also have a `piece of code`", text_type_text)
        expected = [
            TextNode("These are images ", "text"), 
            TextNode("alt text", "image", "https://www.boot.dev"), 
            TextNode(" and ", "text"), 
            TextNode("alt text 2", "image", "https://www.youtube.com/@bootdotdev"),
            TextNode(" but surprise! we also have a `piece of code`", "text")
            ]
        actual = split_nodes_image([node])
        self.assertEqual(actual, expected)


class TestSplitNodesLink(unittest.TestCase):
    def test_split_node_link(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
        )
        expected = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        actual = split_nodes_link([node])
        self.assertEqual(actual, expected)

    def test_split_node_link_embedded_italics(self):
        node = TextNode(
        "This is *italics text* with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
        )
        expected = [
            TextNode("This is *italics text* with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        actual = split_nodes_link([node])
        self.assertEqual(actual, expected)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", "text", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an ", "text", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a ", "text", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an ", "text", None), 
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", "text", None), 
            TextNode("link", "link", "https://boot.dev")
        ]  
        actual = text_to_textnodes(text)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()