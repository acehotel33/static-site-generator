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
        html = open_tag + self.value + close_tag
        return html

main()