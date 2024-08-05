from textnode import TextNode

def main():
    child1 = LeafNode("h2", "Title of paragraph")
    child2 = LeafNode("p", "Hello paragraph", {"href": "hey.com", "key": "value"})
    node1 = HTMLNode("h1", "Title of paragraph", None , {"target": "_blank", "some_key": "some_value"})
    parentnode = ParentNode("div", [child1, child2], {"className": "parentClass", "property": "awesome"})
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    boldtext = TextNode('This is bold', 'bold')
    boldtext_to_leaf = text_node_to_html_node(boldtext)
    print(boldtext_to_leaf.to_html())

    codetext = TextNode('code beep boop', 'code')
    codetext_to_leaf = text_node_to_html_node(codetext)
    print(codetext_to_leaf.to_html())

    linktext = TextNode('Click to download', 'link', 'www.download.com')
    linktext_to_leaf = text_node_to_html_node(linktext)
    print(linktext_to_leaf.to_html())

    imagetext = TextNode('Alt text for image', 'image', 'www.image.com')
    imagetext_to_leaf = text_node_to_html_node(imagetext)
    print(imagetext_to_leaf.to_html())

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})'         

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        prop_string = ""
        for prop in self.props:
            new_prop = f" {prop}" + "=" + f"\"{self.props[prop]}\""
            prop_string += new_prop
        return prop_string

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children==None:
            raise ValueError("Parent node needs children!")
        if tag==None:
            raise ValueError("Parent node needs a tag!")
        super().__init__(tag, None, children, props)

    def to_html(self):
        open_tag = f"<{self.tag}{self.props_to_html()}>"
        body = ""
        for child in self.children:
            child_body = child.to_html()
            body += child_body
        close_tag = f"</{self.tag}>"
        html = open_tag + body + close_tag
        return html

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value==None:
            raise ValueError("Leaf node needs a value!")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag==None:
            return self.value
        open_tag = f"<{self.tag}{self.props_to_html()}>"
        close_tag = f"</{self.tag}>"
        if self.tag=="img":
            close_tag = ""
        html = open_tag + self.value + close_tag
        return html

def text_node_to_html_node(text_node):
    possible_types = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in possible_types:
        raise Exception("Incompatible text node type")
    value = text_node.text
    props = None
    if text_node.text_type == "text":
        tag = None
    elif text_node.text_type == "bold":
        tag = "b"
    elif text_node.text_type == "italic":
        tag = "i"
    elif text_node.text_type == "code":
        tag = "code"
    elif text_node.text_type == "link":
        tag = "a"
        props = {"href": text_node.url}
    elif text_node.text_type == "image":
        tag = "img"
        props = {"src": text_node.url, "alt": text_node.text}
        value = ""
    leaf_node_of_text = LeafNode(tag, value, props)
    return leaf_node_of_text


if __name__ == "__main__":
    main()