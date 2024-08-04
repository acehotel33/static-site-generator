def main():
    example = TextNode('hi', 'bold')
    example2 = TextNode('no', 'bold')
    example3 = TextNode('hi', 'bold')
    example4 = TextNode('','')
    dummy = TextNode('This is a text node', 'bold', 'https://www.boot.dev')

    print(example.__repr__())
    print(example2.__repr__())
    print(dummy.__repr__())


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text # str: content
        self.text_type = text_type # str: "bold" or "italic" etc
        self.url = url # url of the image, default: None

    def __eq__(self, other):
        return (self.text == other.text) & (self.text_type == other.text_type) & (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"






main()