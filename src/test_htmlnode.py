import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Hello paragraph", None, {"href": "hey.com", "key": "value"})
        expected_html = ' href="hey.com" key="value"' 
        actual_html = node.props_to_html()
        self.assertEqual(expected_html, actual_html)

    def test_props_to_html_children(self):
        child1 = HTMLNode()
        child2 = HTMLNode("h2")
        node = HTMLNode("h1", "Title of paragraph",[child1, child2], {"target": "_blank", "some_key": "some_value"})
        expected_html = ' target="_blank" some_key="some_value"'
        actual_html = node.props_to_html()
        self.assertEqual(expected_html, actual_html)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        actual = leafnode.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actual, expected)

    def test_to_html_multiple_props(self):
        leafnode = LeafNode("p", "Hit me!", {"href": "https://www.google.com", "key": "value"})
        actual = leafnode.to_html()
        expected = '<p href="https://www.google.com" key="value">Hit me!</p>'
        self.assertEqual(actual, expected)

    def test_to_html_no_props(self):
        leafnode = LeafNode("p", "This is a paragraph of text")
        actual = leafnode.to_html()
        expected = "<p>This is a paragraph of text</p>"
        self.assertEqual(actual, expected)


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(actual, expected)

    def test_to_html_nested_parent(self):
        node2 = ParentNode(
            "div", 
            [LeafNode("a", "Link!", {"href":"www.link.com"})]
        )
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                node2,
                LeafNode("i", "italic text"),
                LeafNode("img", "", {"src": "www.image.com", "alt": "Alt Text"}),
            ],
        )
        actual = node.to_html()
        expected = '<p><b>Bold text</b><div><a href="www.link.com">Link!</a></div><i>italic text</i><img src="www.image.com" alt="Alt Text"></p>'
        self.assertEqual(actual, expected)

    def test_to_html_image_node_to_leaf(self):
        image_node = TextNode('Alt text for image', 'image', 'www.image.com')
        image_leaf_node = text_node_to_html_node(image_node)
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                image_leaf_node,
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = '<p><b>Bold text</b><img src="www.image.com" alt="Alt text for image"><i>italic text</i>Normal text</p>'
        self.assertEqual(actual, expected)


class TestTextToLeafNode(unittest.TestCase):
    def text_to_leaf(self):
        text = TextNode('This is text')
        text_to_leaf = text_node_to_html_node(text)
        actual = text_to_leaf.to_html()
        expected = "This is text"
        self.assertEqual(actual, expected)

    def bold_to_leaf(self):
        boldtext = TextNode('This is bold', 'bold')
        boldtext_to_leaf = text_node_to_html_node(boldtext)
        actual = boldtext_to_leaf.to_html()
        expected = "<b>This is bold</b>"
        self.assertEqual(actual, expected)

    def code_to_leaf(self):
        codetext = TextNode('code beep boop', 'code')
        codetext_to_leaf = text_node_to_html_node(codetext)
        actual = codetext_to_leaf.to_html()
        expected = "<code>code beep boop</code>"
        self.assertEqual(actual, expected)

    def link_to_leaf(self):
        linktext = TextNode('Click to download', 'link', 'www.download.com')
        linktext_to_leaf = text_node_to_html_node(linktext)
        actual = linktext_to_leaf.to_html()
        expected = '<a href="www.download.com">Click to download</a>'
        self.assertEqual(actual, expected)

    def image_to_leaf(self):
        imagetext = TextNode('Alt text for image', 'image', 'www.image.com')
        imagetext_to_leaf = text_node_to_html_node(imagetext)
        actual = imagetext_to_leaf.to_html() 
        expected = '<img src="www.image.com" alt="Alt text for image">'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()