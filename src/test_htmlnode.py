import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Hello paragraph", None, {"href": "hey.com", "key": "value"})
        expected_html = ' href="hey.com" key="value"' 
        actual_html = node.props_to_html()

        child1 = HTMLNode()
        child2 = HTMLNode("h2")
        node2 = HTMLNode("h1", "Title of paragraph",[child1, child2], {"target": "_blank", "some_key": "some_value"})
        expected_html2 = ' target="_blank" some_key="some_value"'
        actual_html2 = node2.props_to_html()

        self.assertEqual(expected_html, actual_html)
        self.assertEqual(expected_html2, actual_html2)