import unittest

from extract import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        actual = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(actual, expected)

    def test_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)

    def test_images_multiple_missing_opening_bracket(self):
        text = "This is text with a !rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_images(text)
        expected = [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)

    def test_images_multiple_missing_closing_bracket(self):
        text = "This is text with a ![rick roll(https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        with self.assertRaises(Exception) as context:
            extract_markdown_images(text)
        self.assertEqual(str(context.exception), "Incorrect Markdown syntax: missing '[' or ']'")

    def test_images_multiple_missing_opening_parenthesis(self):
        text = "This is text with a ![rick roll]https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        with self.assertRaises(Exception) as context:
            extract_markdown_images(text)
        self.assertEqual(str(context.exception), "Incorrect Markdown syntax: missing '(' or ')'")

    def test_images_multiple_missing_closing_parenthesis(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        with self.assertRaises(Exception) as context:
            extract_markdown_images(text)
        self.assertEqual(str(context.exception), "Incorrect Markdown syntax: missing '(' or ')'")
    
    def test_image_extract_from_link(self):
        text = "This is link [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        actual = extract_markdown_images(text)
        expected = []
        self.assertEqual(actual, expected)

    def test_link_extract_from_image(self):
        text = "This is image ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        actual = extract_markdown_links(text)
        expected = []
        self.assertEqual(actual, expected)