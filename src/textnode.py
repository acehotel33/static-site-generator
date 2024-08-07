import re
from extract import extract_markdown_images, extract_markdown_links


def main():
    node = TextNode(
    "These are images ![alt text](https://www.boot.dev) and ![alt text 2](https://www.youtube.com/@bootdotdev)", text_type_text)
    new_nodes = split_nodes_image([node])
    # print(new_nodes)

    node2 = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
    )
    new_nodes2 = split_nodes_link([node2])
    print(new_nodes2)

text_type_text="text"
text_type_code="code"
text_type_bold="bold"
text_type_italic="italic"
text_type_link="link"
text_type_image="image"

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
            list_of_text_and_images = re.split(r"(!\[.*?\]\(.*?\))", node.text)
            
            for item in list_of_text_and_images:
                extracted_image_tuples = extract_markdown_images(item)
                if len(extracted_image_tuples) == 0:
                    if item != "":
                        new_nodes.append(TextNode(item, text_type_text))
                        
                else:
                    for image_tuple in extracted_image_tuples:
                        new_nodes.append(TextNode(image_tuple[0], text_type_image, image_tuple[1]))
                        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            list_of_text_and_links = re.split(r"(\[.*?\]\(.*?\))", node.text)

            for item in list_of_text_and_links:
                extracted_link_tuples = extract_markdown_links(item)
                if len(extracted_link_tuples) == 0:
                    if item != "":
                        new_nodes.append(TextNode(item, text_type_text))
                else:
                    for link_tuple in extracted_link_tuples:
                        new_nodes.append(TextNode(link_tuple[0], text_type_link, link_tuple[1]))

    return new_nodes

if __name__ == "__main__":
    main()



"""

[
TextNode(These are images , text, None), 
TextNode(alt text, image, https://www.boot.dev), 
TextNode( and , text, None), 
TextNode(alt text 2, image, https://www.youtube.com/@bootdotdev)]


"""


"""
[
TextNode(This is text with a link , text, None), 
TextNode(to boot dev, link, https://www.boot.dev), 
TextNode( and , text, None), 
TextNode(to youtube, link, https://www.youtube.com/@bootdotdev)]
"""