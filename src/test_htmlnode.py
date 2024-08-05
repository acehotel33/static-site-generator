import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = '<p><b>Bold text</b><div><a href="www.link.com">Link!</a></div><i>italic text</i>Normal text</p>'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()