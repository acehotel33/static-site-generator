from extract import extract_markdown_images, extract_markdown_links


def main():
    example = TextNode('hi', 'bold')
    example2 = TextNode('no', 'bold')
    example3 = TextNode('hi', 'bold')
    example4 = TextNode('','')
    dummy = TextNode('This is a text node', 'bold', 'https://www.boot.dev')

    node1 = TextNode("`code block` at the start and `at the end`", text_type_text)
    # new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    # print(new_nodes)
    node2 = TextNode("This is text with a `code block` word", text_type_text)
    # new_nodes2 = split_nodes_delimiter([node2], "`",  text_type_code)
    
    node3 = TextNode("This is a regular text", text_type_text)
    new_nodes = split_nodes_delimiter([node1, node2, node3], "`", text_type_code)
    print(new_nodes)


text_type_text="text"
text_type_code="code"
text_type_bold="bold"
text_type_italic="italic"



class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text # str: content
        self.text_type = text_type # str: "bold" or "italic" etc
        self.url = url # url of the image, default: None

    def __eq__(self, other):
        return (self.text == other.text) & (self.text_type == other.text_type) & (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise Exception('Node has invalid Markdown syntax: missing opening or closing delimiter')
        if node.text_type != "text":
            new_nodes.append(node)
        else:    
            split_text = node.text.split(delimiter)
            identifier = []
            nodes = []
            for i in range(len(split_text)):
                if i % 2 == 0:
                    if split_text[i] != "":
                        nodes.append(TextNode(split_text[i], text_type_text))
                else:
                    if split_text[i] != "": 
                        nodes.append(TextNode(split_text[i], text_type))
            new_nodes.extend(nodes) 
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            links_list_of_tuples = extract_markdown_links(node.text)
            images_list_of_tuples = extract_markdown_images(node.text)
    return new_nodes

if __name__ == "__main__":
    main()